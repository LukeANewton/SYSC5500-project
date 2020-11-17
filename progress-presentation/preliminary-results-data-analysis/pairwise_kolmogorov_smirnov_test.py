# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:16:29 2020

@author: luken
"""
import math
import matplotlib.pyplot as plt

confidence_level = 0.05
filenames = ["botnet1times.txt", "botnet2times.txt", "botnet3times.txt", 
             "botnet4times.txt", "botnet5times.txt"]

def kolmogorov_smirnov_test(observations1, observations2, confidence_level):
    assert len(observations1) > 0
    assert len(observations1) == len(observations2)
    
    cdf1 = list()
    cdf2 = list()
    n = len(observations1)
    m = len(observations2)
    
    #compute cdf for each empirical distribution
    for i in range(100):
        cdf1.append(sum(1 for x in observations1 if x <= i))
        cdf2.append(sum(1 for x in observations2 if x <= i))
    for i in range(len(cdf1)):
        cdf1[i]/=len(observations1)
        cdf2[i]/=len(observations2)
       
    difference = list()
    for i in range(len(cdf1)):
        difference.append(abs(cdf1[i] - cdf2[i]))
    
    threshold = math.sqrt(-0.5*math.log(confidence_level/2)) * math.sqrt((n+m)/(n*m))
    print()
    print('threshold:', threshold, 'D:',max(difference))
    return threshold > max(difference)


observations = list()
for filename in filenames:
    with open(filename) as f:
        content = f.readlines()
    #remove endlines
    content = [x.strip() for x in content] 
    # remove 0 values
    content = [x for x in content if not x.endswith('0.0')]
    # remove values for time 100
    content = [x for x in content if not x.startswith('100')]
    #take only the first value after each comment
    data = list()
    for i in range(len(content)-1):
        if content[i].startswith("#"):
            data.append(content[i+1])
    #remove trailing 1.0
    data = [x[:-4] for x in data] 
    #convert to numbers and sort
    data = [float(x) for x in data] 
    observations.append(sorted(data))

print("pairwise Kolmogorov–Smirnov test:")
for i in range(len(observations)):
    for j in range(i+1, len(observations)):
        print(i, " and ", j, " are likely", 
              " not" if 
              not kolmogorov_smirnov_test(observations[i], observations[j], confidence_level)
              else "",
              " drawn from the same distribution", sep="")