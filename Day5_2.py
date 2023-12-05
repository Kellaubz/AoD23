#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def cut_range(interval,line):
    a=interval[0]
    b=interval[1]
    c=line[1]
    d=line[1]+line[2]-1
    if c>b or d<a:
        return [[a,b]],[]
    elif c<=a and d>=b:
        return [],[[line[0]+a-c,line[0]+b-c]]
    elif c<=a and d<b:
        return [[d+1,b]],[[line[0]+a-c,line[0]+d-c]]
    elif c>a and d>=b:
        return [[a,c]],[[line[0],line[0]+b-c]]
    elif c>a and d<b:
        return [[a,c],[d+1,b]],[[line[0],line[0]+d-c]]

def range_locations(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    seeds=re.findall('\d+',lines[0])
    range_seeds=[]
    processed_seeds=[]
    for i in range((len(seeds))//2):
        range_seeds.append([int(seeds[2*i]),int(seeds[2*i])+int(seeds[2*i+1])-1])
    for i in range(3,len(lines)):
        line=re.findall('\d+',lines[i])
        if len(line)==0:
            if processed_seeds!=[]:
                range_seeds=processed_seeds
            processed_seeds=[]
        else:
            for j in range(len(line)):
                line[j]=int(line[j])
            new_range_seeds=[]
            while range_seeds!=[]:
                seed=range_seeds.pop()
                a,b=cut_range(seed,line)
                new_range_seeds=new_range_seeds+a
                processed_seeds=processed_seeds+b
            range_seeds=new_range_seeds
    m=min([processed_seeds[i][0] for i in range(len(processed_seeds))])
    return m
    