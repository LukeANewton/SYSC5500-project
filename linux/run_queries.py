import os
import time
import math
from datetime import datetime
from set_num_devices import set_num_devices
from shutil import copyfile

# ------------------------------------------------------------
#             Step 1: set simulation parameters
# ------------------------------------------------------------
MODEL_NAME = 'model.xml'
QUERY_NAME = 'messages-and-bot-size.q'

NUMBER_DEVICES = 100

# proportions should sum to one, this is checked in the python script
PROPORTION_ALWAYS_ON = 0
PROPORTION_PERIODIC_REBOOT = 1

# these values are only relevant for devices that reboot periodically
REBOOT_LENGTH = 600
REBOOT_PERIOD = 36000

NUMBER_CREDENTIALS = 62

SIMULATION_TIME = 864000
SIMULATION_RUNS = 1

STOP_WHEN_ALL_INFECTED = False

# ------------------------------------------------------------
#             Step 2: edit model files and run simulation
#     (do not change this if you're just running simulations!)
# ------------------------------------------------------------
results_folder = str(datetime.now()).replace(' ', '_')
os.mkdir(results_folder)

for number_devices in [10, 25, 50, 100]:
  for proportion_always_on in [0, 0.25, 0.5, 0.75, 1]:
    proportion_periodic_reboot = 1 - proportion_always_on
    for period_of_reboot in [3000, 6000, 18000, 36000, 864000]:
      for rtt, rtt_scale in {'100ms':1, '1s':0.1}.items():
        for stealthing_scale in [0.01, 0.1, 0.5, 1]:
          simulation_time = int(SIMULATION_TIME * stealthing_scale)
          reboot_length = math.ceil(REBOOT_LENGTH * rtt_scale * stealthing_scale)
          reboot_period = int(period_of_reboot * rtt_scale * stealthing_scale)
          
          print('Starting experiment with:')
          print('\t', str(number_devices), 'devices')
          print('\t', str(proportion_periodic_reboot*100), '% of devices rebooting')
          print('\t', 'bots are active', str(stealthing_scale*100), '% of the time')
          print('\t', 'a reboot period of', str(reboot_period), 'time units')
          print('\t', 'a reboot length of', str(reboot_length), 'time units')
          print('\t', 'simulating', str(simulation_time), 'time units')
          
          # call the python helper file to edit model system declaration
          set_num_devices(number_devices, proportion_always_on, proportion_periodic_reboot, reboot_length, reboot_period, NUMBER_CREDENTIALS, MODEL_NAME)         
                       
          # make a folder to move all output CSVs, along with a copy of the model and query used
          directory_name = str(datetime.now()).replace(' ', '_')
          model_path = results_folder + '/' + directory_name + '/' + MODEL_NAME
          query_path = results_folder + '/' + directory_name + '/' + QUERY_NAME 
          os.mkdir(results_folder + '/' + directory_name)
          copyfile(os.getcwd() + '/' + MODEL_NAME, os.getcwd() + '/' + model_path)
          
          # create a query file
          QUERY_NAME = 'query.q'
          with open(query_path, "w") as file:
            file.write('simulate [total_time<=' + str(simulation_time) + '; ' + str(SIMULATION_RUNS) + '] {current_number_bots, 2*((attempt_loops+scan_loops)*LIMIT + total_attempts + total_scans)}' + (' : current_number_bots==total_devices-1' if STOP_WHEN_ALL_INFECTED else ''))
          
          # wait until the files have been properly copied to results folder
          while(not(os.path.exists(model_path) and os.path.exists(query_path))):
            time.sleep(0.5)            
                              
          # run the verifier query
          command = './verifier/verifyta -T -S 3 -O csv ' + model_path + ' ' + query_path
          print('running: ' + command)
          start_time = time.time()
          os.system(command)
          end_time = time.time()
          
          # record how long simulation takes
          print("--- %s seconds ---" % (end_time - start_time))
          with open(results_folder + '/' + directory_name + '/sim_time.txt', "w") as file:
            file.write(str(end_time - start_time) + ' seconds')
            
          # record simulation parameters
          with open(results_folder + '/' + directory_name + '/parameters.txt', "w") as file:
            file.write(str(number_devices)+' devices '+str(proportion_periodic_reboot)+' rebooting_every '+str(reboot_period/(10*rtt_scale*stealthing_scale))+' with '+str(stealthing_scale)+' efficiency')
