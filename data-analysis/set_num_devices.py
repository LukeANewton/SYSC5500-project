# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:41:47 2020

@author: luken

This script aids in the build process for our UPPAAL model.

The script will read in the UPPAAL xml model file and replace the system
declaration with a new declaration determined by a number of specified system
parameters. This means that we do need to manually edit anything in 
the model file when we want to change the number of devices in the network.
Passwords and 1st reboot times (for periodic rebooting) are selected unifomly 
randomly.

This is helpful for larger models becuase unfortunately, UPPAAL does not 
support use of looping or arrays in their system declarations, so you need a 
separate line to instantiate each device in the model.

this file is executed from 'run_query.sh'. Its recommended to us that file for
simulation runs rather than executing this directly
"""
import random
import math
import sys

NUMBER_DEVICES = int(sys.argv[1])
PROPORTION_ALWAYS_ON = float(sys.argv[2])
PROPORTION_PERIODIC_REBOOT = float(sys.argv[3])

REBOOT_LENGTH = int(sys.argv[4])
REBOOT_PERIOD = int(sys.argv[5])

NUMBER_CREDENTIALS = int(sys.argv[6])


assert PROPORTION_ALWAYS_ON + PROPORTION_PERIODIC_REBOOT == 1

# this is necessary becasue UPPAAL integers are 16bit signed
LIMIT = 32000
PERIOD_OVERFLOWS = REBOOT_PERIOD // LIMIT
REBOOT_PERIOD = REBOOT_PERIOD % LIMIT
# ------------------------------------------------------------
#                 Step 1: get the model file
# ------------------------------------------------------------
model_name = sys.argv[7]

# ------------------------------------------------------------
#          Step 2: build system declaration string
# ------------------------------------------------------------

# this is the part of model initialization that does not change based on the number of bots
init_string = "MIRAI_BLCK = Mirai_Blacknet();BOT_DF = Bot_Default(0,110);"

# add the always-connected devices first with random selected credentials
num_always_connected_devices = math.floor(PROPORTION_ALWAYS_ON*(NUMBER_DEVICES+1))
for i in range(1, num_always_connected_devices):
    init_string += "BOT"+str(i)+" = Bot_t1("+str(i)+","+str(random.randint(101, 100+NUMBER_CREDENTIALS))+");"
 
# add the devices with periodic reboot
force_reboot_initialization = ""
for i in range(num_always_connected_devices if num_always_connected_devices > 0 else 1, NUMBER_DEVICES+1):
    first_reboot_time = random.randint(1, REBOOT_PERIOD+LIMIT*PERIOD_OVERFLOWS)
    time_overflows = first_reboot_time // LIMIT
    first_reboot_time = first_reboot_time % LIMIT
    init_string += "BOT"+str(i)+" = Bot_t2("+str(i)+","+str(random.randint(101, 100+NUMBER_CREDENTIALS))+","+str(REBOOT_LENGTH)+","+str(REBOOT_PERIOD)+","+str(PERIOD_OVERFLOWS)+","+str(first_reboot_time)+","+str(time_overflows)+");"
    
# this part again, does not change based on the number of devices in the network
init_string += "system MIRAI_BLCK, BOT_DF,"

# append list of instantiated bots to system declaration
for i in range(1, NUMBER_DEVICES):
    init_string +=" BOT"+str(i)+","
init_string += " BOT"+str(NUMBER_DEVICES)+";"

# to make this more readable, we add newlines after each semi-colon.
# we could hard code these  above, but its easier to read the above 
# code if we do this separately
init_string = init_string.replace(';', ';\n')

# ------------------------------------------------------------
#     Step 3: insert system declaration into model file
# ------------------------------------------------------------

# read in file
contents = ''
with open(model_name, 'r') as file:
    contents = file.read()
    
# get the start and end locations of the system declaration
start = contents.find('<system>') + len('<system>')
end = contents.find('</system>')

# replace system declaration with new generated declaration
contents = contents.replace(contents[start:end], init_string)

# ------------------------------------------------------------
# Step 4: change the number of devices in variable declaration
# ------------------------------------------------------------
start = contents.find('const int total_devices =') + len('const int total_devices =')
end = contents.find(';', start)
contents = contents.replace(contents[start:end], str(NUMBER_DEVICES+1), 1)

# ------------------------------------------------------------
#           Step 5: write new file contents
# ------------------------------------------------------------
with open(model_name, "w") as file:
    file.write(contents)