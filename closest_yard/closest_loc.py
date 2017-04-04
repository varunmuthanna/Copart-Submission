# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 12:32:43 2017

@author: varun
"""

import csv
import math
import random
import sys

#Euclidean distance is taken
def distance_bw_points(loc1x,loc1y, loc2x,loc2y):
    return math.sqrt(math.pow(math.fabs(loc1x-loc2x),2) + math.pow(math.fabs(loc1y-loc2y),2))

#get random points as the initial centroid
def getInitialCentroids(location,num_entry):
    num_clusters = num_entry/1000
    centroid = []
    clus_index = 0
    for i in range(0,num_clusters):
        index = random.randint(1,num_entry-2)
        if(index < 1 or index > num_entry-2):
            print index
        if location[index][1] == "":
            continue
        
        if location[index][2] == "":
            continue
        centroid.append([])
        centroid[clus_index].append(float(location[index][1]))
        centroid[clus_index].append(float(location[index][2]))
        clus_index = clus_index + 1
    return centroid

# based on the centroid add the points to closest centroid
def updatecentroidcluster(centroid,location,num_entry):
    num_clusters = len(centroid)
    for i in range(1,num_entry):
        if location[i][1] == "":
            continue
        
        if location[i][2] == "":
            continue
        
        lat = float(location[i][1])
        lon = float(location[i][2])
        min_in = -1;
        min_val = 100000;
        for j in range(0,num_clusters):
            val1 = centroid[j][0]
            val2 = centroid[j][1]
            dist = distance_bw_points(lat,lon,val1,val2)
            if(dist < min_val):
                min_val = dist
            min_in = j
            
        centroid[min_in].append(i)
    return centroid

#take the average of longitude and latitude for new centroid point
def getnewcentroid(centroid,location,num_entry):
    num_cluster = len(centroid)
    newcentroid = []
    clus_index = 0
    for i in range(0,num_cluster):
        num_val = len(centroid[i])
        lat = 0
        lon = 0
        index = 2
        while(index < num_val-1):
            lat = lat + float(location[centroid[i][index]][1])
            lon = lon + float(location[centroid[i][index+1]][2])
            index = index+2
        newcentroid.append([])
        newcentroid[clus_index].append(lat)
        newcentroid[clus_index].append(lon)
        clus_index = clus_index + 1
        
    return newcentroid
        
in_lat = float(sys.argv[1])
in_log = float(sys.argv[2])

location = list(csv.reader(open('zip_codes_states.csv','r'),delimiter=','))

num_entry = len(location)
num_col = len(location[0])

#this part of the code runs in O(N) time
min = 100000.0
min_index = 0
for i in range(2,num_entry):
    if location[i][1] == "":
        continue
    
    if location[i][2] == "":
        continue

    dist = distance_bw_points(in_lat,in_log,float(location[i][1]),float(location[i][2]))
    if(dist < min):
        min = dist
        min_index = i

print "yard location is zip = "+location[min_index][0]+" city="+location[min_index][3]+" state= "+location[min_index][4]+" county = "+location[min_index][5]+""

#Below part is the optimizedversion implementing the unsupervised
#learning,.Here I have used Kmeans algorithm
centroid = getInitialCentroids(location,num_entry)
for i in range(0,2):
    centroid = updatecentroidcluster(centroid,location,num_entry)
    centroid = getnewcentroid(centroid,location,num_entry)

centroid = updatecentroidcluster(centroid,location,num_entry)

min_val = 100000.0
min_index = 0
num_clusters = len(centroid)
for i in range(0,num_clusters):
    val1 = centroid[i][0]
    val2 = centroid[i][1]
    dist = distance_bw_points(in_lat,in_log,val1,val2)
    if(dist < min_val):
        min_val = dist
    min_index = i

closecentroid = centroid[min_index]
num_index = len(closecentroid)
index = 2
while(index < num_index-1 and index < 2):
    print "yard location is zip = "+location[index][0]+" city="+location[index][3]+" state= "+location[index][4]+" county = "+location[index][5]+""
    
    
    

