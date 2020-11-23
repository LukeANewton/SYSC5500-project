# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:04:03 2020

@author: luken

This short script will graph the simulation result data. This is appropriate 
to use when grahping different query results ont he same axes.

It is assumed that each results folder has two CSVs: one for the number of 
infected devices, and the second has total messages sent over time

Note that numpy and matplotlib are NOT standard python libraries. You need to
install these packages separately, or use the Anaconda distribution of python.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob

# the name for the graph of botnet size vs time
BOTNET_SIZE_NAME='Botnet growth over time for networks of 100, 250, and 500 devices'
# the name for the graph of total messages sent vs time
MESSAGE_PASSING_NAME='Total messages sent for networks of 100, 250, and 500 devices'

# if true, the botnet size graph shows the percentage of devices infected
# if false, the botnet size graph shows the number of devices infected
CALCULATE_PROPORTION=False
#if CALCULATE_PROPORTION is true, we need the number of devices here as well
NUMBER_DEVICES=100

#this is only the prefix result folders have, since they are also timestamped
RESULTS_FOLDER = 'messages-and-bot-size'


# ------------------------------------------------------------
#                 Step 1: get the simulation data
# ------------------------------------------------------------
RESULTS_FOLDERS = glob(RESULTS_FOLDER+'*/')
data = list()

for folder in RESULTS_FOLDERS:
    files = os.listdir(folder)
    d = list()
    for f in files:
        if f.endswith('csv'):
            d.append(np.genfromtxt(folder+'/'+f, delimiter = ','))
    data.append(d)

# ------------------------------------------------------------
#                 Step 2: graph each data set
# ------------------------------------------------------------
def set_graph(name, y_axis_label):
    plt.figure()
    plt.ylabel(y_axis_label) 
    plt.xlabel('time')  
    plt.title(name)
    plt.grid()
    return plt.axes()
    

ax = set_graph(BOTNET_SIZE_NAME, 
          'proportion devices infected' if CALCULATE_PROPORTION else 'devices infected')
for d in data:
    ax.plot(d[0][:, 0], 
           d[0][:, 1]/NUMBER_DEVICES if CALCULATE_PROPORTION else d[0][:, 1])
plt.show()

ax = set_graph(MESSAGE_PASSING_NAME, 'total messages sent')
for d in data:
    ax.plot(d[1][:, 0], d[1][:, 1])
plt.show()

