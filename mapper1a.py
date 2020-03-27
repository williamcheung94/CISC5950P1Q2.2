#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:57:47 2020

@author: Nicola
"""
import csv
import math
import sys
from random import randint

def eudistance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

#initalize list of centroids
def centroidinit(num):
    SHOT_DIST_max=47
    SHOT_DIST_min=0
    CLOSE_DEF_DIST_max=53
    CLOSE_DEF_DIST_min=0
    SHOT_CLOCK_max=24
    SHOT_CLOCK_min=0
    initialcenters=[]
    for center in range(1,num+1):
        initialcenters.append((center,(randint(SHOT_DIST_min,SHOT_DIST_max),randint(CLOSE_DEF_DIST_min,CLOSE_DEF_DIST_max),randint(SHOT_CLOCK_min,SHOT_CLOCK_max))))
    return initialcenters

#create centroid dictionary
def reccreate(initialcenters):
    record={}
    for num in range(len(initialcenters)):
        record[initialcenters[num][1]]=[0,0,0,0]
    return record

def clustersum(initialcenters, player, record):
    for row in sys.stdin:
        if row[19].replace(',', '').lower()==player:
            try:
                sample=(float(row[11]),float(row[16]),float(row[8]))
                sampleclass=None
                for num in range(len(initialcenters)):
                    if sampleclass==None:
                        sampleclass=initialcenters[0][1]
                    elif eudistance(initialcenters[num][1],sample)<eudistance(sampleclass,sample):
                        sampleclass=initialcenters[num][1]
                    else:
                        continue
                record[sampleclass]=[x + y for x, y in zip(record.get(sampleclass), (float(row[11]),float(row[16]),float(row[8]),1))]
            except:
                #print('fail')
                continue
    return record
 
def centerlist(initalcenters):
    defaultcenters=[]
    for i in initialcenters:
        defaultcenters.append(i[1])
    return defaultcenters
   
    
if __name__ == "__main__":
    player = sys.argv[1]
    initialcenters=centroidinit(4)
    initrecords=reccreate(initialcenters)
    records=clustersum(initialcenters, player, initrecords)
    defcenters= centerlist(initialcenters)  
                 
    for i in records.items():
        print ('%s\t%s\t%s' % (i[0], i[1],defcenters))

