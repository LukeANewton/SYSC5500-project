import os
import time
from datetime import datetime
from set_num_devices import set_num_devices
from shutil import copyfile           
     
     
NUMBER_DEVICES = 'number devices'
PROPORTION_ALWAYS_ON = 'proportion always on'  
REBOOT_LENGTH = 'reboot length'
REBOOT_PERIOD = 'reboot period'
PROPORTION_TIME_ACTIVE = 'time active'
MODEL_NAME = 'model_name'
STOP_WHEN_ALL_INFECTED = 'stop if all infected' 
SIMULATION_TIME = 'simulation time'    
            
QUERY_NAME = 'messages-and-bot-size.q'
NUMBER_CREDENTIALS = 62
SIMULATION_RUNS = 1


def run_query(num_devices, proportion_always_on, reboot_length, reboot_period, proportion_of_time_active, model_name, stop_if_all_infected, simulation_time):
	print('Starting experiment with:')
	print('\t', str(num_devices), 'devices')
	print('\t', str((1-proportion_always_on)*100), '% of devices rebooting')
	print('\t bots spend', str((1-proportion_of_time_active)*100), '% of time spent hibernating')
	print('\t', 'a reboot period of', str(reboot_period), 'time units')
	print('\t', 'a reboot length of', str(reboot_length), 'time units')
	print('\t', 'simulating', str(simulation_time), 'time units')

	# call the python helper file to edit model system declaration
	set_num_devices(num_devices, proportion_always_on, 1-proportion_always_on, 
			int(max(reboot_length*proportion_of_time_active, 1)), 
			int(max(reboot_period*proportion_of_time_active, 1)),
			NUMBER_CREDENTIALS, model_name)

	# make a folder to move all output CSVs, along with a copy of the model and query used
	directory_name = str(num_devices) + '_devices_with_' + str(1-proportion_always_on) + '_peiodicaly_rebooting_every_' + str(reboot_period) + '_time_units_'+str(datetime.now()).replace(' ', '_')
	os.mkdir(directory_name)
	copyfile(os.getcwd() + '/' + model_name, os.getcwd() + '/' + directory_name + '/' + model_name)

	# create a query file
	QUERY_NAME = 'query.q'
	with open(directory_name + '/' + QUERY_NAME, "w") as file:
	    file.write('simulate [total_time<=' + str(simulation_time) + '; ' + str(SIMULATION_RUNS) +
		       '] {current_number_bots, 2*((attempt_loops+scan_loops)*LIMIT + total_attempts + total_scans)}' +
		       (' : current_number_bots==total_devices-1' if stop_if_all_infected else ''))

	# run the verifier query
	command = './verifier/verifyta -o 2 -C -S 3 -O csv \'' + directory_name + '/' + model_name + '\' \'' + directory_name + '/' + QUERY_NAME + '\''
	print('running: ' + command)
	start_time = time.time()
	os.system(command)
	end_time = time.time()

	# record how long simulation takes
	print("--- %s seconds ---" % (end_time - start_time))
	with open(directory_name + '/sim_time', "w") as file:
		file.write(str(end_time - start_time) + ' seconds')


# all always-connected devices on a fixed-delay network
#run_query(2000, 1, 600, 36000, 'model-fixed-speed.xml', True, 864000)

# all rebooting devices for different reboot periods on a fixed-delay network (100ms)
fixed_speed_queries = [{REBOOT_LENGTH:600, REBOOT_PERIOD:36000, PROPORTION_TIME_ACTIVE:0.5},		
			{REBOOT_LENGTH:600, REBOOT_PERIOD:18000, PROPORTION_TIME_ACTIVE:0.5},
			{REBOOT_LENGTH:600, REBOOT_PERIOD:6000, PROPORTION_TIME_ACTIVE:0.5},
			{REBOOT_LENGTH:600, REBOOT_PERIOD:3000, PROPORTION_TIME_ACTIVE:0.5}]#,
#			{REBOOT_LENGTH:600, REBOOT_PERIOD:864000}]
for query in fixed_speed_queries:
	run_query(500, 0, query[REBOOT_LENGTH], query[REBOOT_PERIOD], query[PROPORTION_TIME_ACTIVE], 'model-fixed-speed.xml', False, 2*query[REBOOT_PERIOD])
	
# all rebooting devices for different reboot periods on a variable-delay network (0ms to 250ms)
#variable_speed_queries = [{REBOOT_LENGTH:240, REBOOT_PERIOD:14400},		
#			{REBOOT_LENGTH:240, REBOOT_PERIOD:7200},
#			{REBOOT_LENGTH:240, REBOOT_PERIOD:2400},
#			{REBOOT_LENGTH:240, REBOOT_PERIOD:1200},
#			{REBOOT_LENGTH:240, REBOOT_PERIOD:345600}]
variable_speed_queries = []#[{REBOOT_LENGTH:240, REBOOT_PERIOD:345600}]
for query in variable_speed_queries:
	run_query(500, 0, query[REBOOT_LENGTH], query[REBOOT_PERIOD], 'model-variable-speed.xml', False, 2*query[REBOOT_PERIOD])
