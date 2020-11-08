# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:37:47 2020

@author: luken
"""
import statistics


filename = "total_messages.txt"

totals = list()

with open(filename) as f:
    content = f.readlines()
    
#remove endlines
content = [x.strip() for x in content] 

#we want the last data point in each run to get the total for the run
for i in range(2, len(content)):
    if content[i].startswith('#'):
        totals.append(content[i-1])

#remove the time from each data point so we are left with just the total
totals = [x.split(' ')[1] for x in totals]
totals = [float(x) for x in totals] 

#calculate confidence interval for expectation
mean = statistics.mean(totals)
std_dev = statistics.stdev(totals)
#1.96 is the z score for 95% confidence
print (mean, "+-", std_dev*1.96)