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


def set_num_devices(number_devices, proportion_always_on, proportion_periodic_reboot, reboot_length, reboot_period,
                    number_credentials, model_name):
    assert proportion_always_on + proportion_periodic_reboot == 1

    # this is necessary because UPPAAL integers are 16bit signed
    LIMIT = 32000
    period_overflows = reboot_period // LIMIT
    reboot_period = reboot_period % LIMIT
    # ------------------------------------------------------------
    #          Step 1: build system declaration string
    # ------------------------------------------------------------

    # this is the part of model initialization that does not change based on the number of bots
    init_string = "CNC=CnC();BOT_DF = Bot_Default(0,110);"

    # add the always-connected devices first with random selected credentials
    num_always_connected_devices = math.floor(proportion_always_on * (number_devices + 1))
    for i in range(1, num_always_connected_devices):
        init_string += "BOT" + str(i) + " = Bot_t1(" + str(i) + "," + str(
            random.randint(101, 100 + number_credentials)) + ");"

    # add the devices with periodic reboot
    force_reboot_initialization = ""
    for i in range(num_always_connected_devices if num_always_connected_devices > 0 else 1, number_devices + 1):
        first_reboot_time = random.randint(1, reboot_period + LIMIT * period_overflows)
        time_overflows = first_reboot_time // LIMIT
        first_reboot_time = first_reboot_time % LIMIT
        init_string += "BOT" + str(i) + " = Bot_t2(" + str(i) + "," + str(
            random.randint(101, 100 + number_credentials)) + "," + str(reboot_length) + "," + str(
            reboot_period) + "," + str(period_overflows) + "," + str(first_reboot_time) + "," + str(
            time_overflows) + ");"

    # this part again, does not change based on the number of devices in the network
    init_string += "system CNC, BOT_DF,"

    # append list of instantiated bots to system declaration
    for i in range(1, number_devices):
        init_string += " BOT" + str(i) + ","
    init_string += " BOT" + str(number_devices) + ";"

    # to make this more readable, we add newlines after each semi-colon.
    # we could hard code these  above, but its easier to read the above
    # code if we do this separately
    init_string = init_string.replace(';', ';\n')

    # ------------------------------------------------------------
    #     Step 2: insert system declaration into model file
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
    contents = contents.replace(contents[start:end], str(number_devices + 1), 1)

    # ------------------------------------------------------------
    #           Step 5: write new file contents
    # ------------------------------------------------------------
    with open(model_name, "w") as file:
        file.write(contents)
