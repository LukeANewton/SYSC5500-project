import os
import time
from datetime import datetime
from set_num_devices import set_num_devices
from shutil import copyfile

# ------------------------------------------------------------
#             Step 1: set simulation parameters
# ------------------------------------------------------------
MODEL_NAME = 'Mirai_blacknet_1.0.xml'
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

# for whatever reason, the verifier wont run with the given name
# this is solved by creating a copy with a new name
NEW_MODEL_NAME = 'model.xml'
os.rename(MODEL_NAME, NEW_MODEL_NAME)

# call the python helper file to edit model system declaration
set_num_devices(NUMBER_DEVICES, PROPORTION_ALWAYS_ON, PROPORTION_PERIODIC_REBOOT, REBOOT_LENGTH, REBOOT_PERIOD,
                NUMBER_CREDENTIALS, NEW_MODEL_NAME)

# make a folder to move all output CSVs, along with a copy of the model and query used
directory_name = str(datetime.now())
os.mkdir(directory_name)
copyfile(os.getcwd() + '/' + NEW_MODEL_NAME, os.getcwd() + '/' + directory_name + '/' + NEW_MODEL_NAME)

# create a query file
QUERY_NAME = 'query.q'
with open(directory_name + '/' + QUERY_NAME, "w") as file:
    file.write('simulate [total_time<=' + str(SIMULATION_TIME) + '; ' + str(SIMULATION_RUNS) +
               '] {current_number_bots, message_loops*LIMIT + total_messages}' +
               (' : current_number_bots==total_devices-1' if STOP_WHEN_ALL_INFECTED else ''))

# run the verifier query
command = './verifier/verifyta -A -T -S 0 -O csv \'' + directory_name + '/' + NEW_MODEL_NAME + '\' \'' + directory_name + '/' + QUERY_NAME + '\''
print('running: ' + command)
start_time = time.time()
os.system(command)
end_time = time.time()

# record how long simulation takes
print("--- %s seconds ---" % (end_time - start_time))
with open(directory_name + '/sim_time', "w") as file:
	file.write(str(end_time - start_time) + ' seconds')

# revert model name change
os.rename(NEW_MODEL_NAME, MODEL_NAME)
