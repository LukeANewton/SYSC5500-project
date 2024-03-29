# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:04:03 2020

@author: luken

This short script will graph the simulation result data. This is appropriate 
to use when the query only ran one simulation run.

The script assumes you will run it after each simulation run, so it just graphs 
the first result folder it finds. The script assumes the first file (alphabetically)
is the bot size values and the second file in the results folder is the number 
of messages.

Note that numpy and matplotlib are NOT standard python libraries. You need to
install these packages separately, or use the Anaconda distribution of python.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# the name for the graph of botnet size vs time
BOTNET_SIZE_NAME='100 device network with daily rebooting'
# the name for the graph of total messages sent vs time
MESSAGE_PASSING_NAME='total messages sent for 100 periodically \nrebooting devices'
# the name of the folder contining the simulation results to graph
RESULTS_FOLDER = '75%-always-connected'

# if true, the botnet size graph shows the percentage of devices infected
# if false, the botnet size graph shows the number of devices infected
CALCULATE_PROPORTION=True
#if CALCULATE_PROPORTION is true, we need the number of devices here as well
NUMBER_DEVICES=100

# if true, the average size of the botnet will be added to the botnet size plot
PLOT_BOTNET_STEADY_STATE_SIZE = True
# ------------------------------------------------------------
#                 Step 1: get the simulation data
# ------------------------------------------------------------
files = os.listdir(RESULTS_FOLDER)
data = list()
for f in files:
    if f.endswith('csv'):
        data.append(np.genfromtxt(RESULTS_FOLDER+'/'+f, delimiter = ','))
    

# ------------------------------------------------------------
#                 Step 2: graph each data set
# ------------------------------------------------------------
def graph(name, y_axis_label, x, y, plot_average_y):
    plt.figure()
    ax = plt.axes()
    plt.ylabel(y_axis_label) 
    plt.xlabel('time')  
    plt.title(name)
    ax.plot(x, y);
    if plot_average_y:
        average = sum(y)/len(y)
        ax.plot(x, [average]*len(y), label=str(average));
        plt.legend()
    plt.grid()
    plt.show()

graph(BOTNET_SIZE_NAME, 
      'proportion devices infected' if CALCULATE_PROPORTION else 'devices infected',
      data[0][:, 0], 
      data[0][:, 1]/NUMBER_DEVICES if CALCULATE_PROPORTION else data[0][:, 1],
      PLOT_BOTNET_STEADY_STATE_SIZE)

graph(MESSAGE_PASSING_NAME, 'total messages sent', 
      data[1][:, 0],  data[1][:, 1], False)

