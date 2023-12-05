#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def seed_locations(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    seeds=re.findall('\d+',lines[0])
    seeds_buffer=[-1]*len(seeds)
    for i in range(len(seeds)):
        seeds[i]=int(seeds[i])
    for i in range(3,len(lines)):
        line=re.findall('\d+',lines[i])
        if len(line)==0:
            for j in range(len(seeds)):
                if seeds_buffer[j]!=-1:
                    seeds[j]=seeds_buffer[j]
            seeds_buffer=[-1]*len(seeds)
        else:
            for j in range(len(line)):
                line[j]=int(line[j])
            for j in range(len(seeds)):
                if seeds[j]>=line[1] and seeds[j]<=line[1]+line[2]-1:
                    seeds_buffer[j]=line[0]-line[1]+seeds[j]
    for j in range(len(seeds)):
        if seeds_buffer[j]!=-1:
            seeds[j]=seeds_buffer[j]
    return min(seeds)
    