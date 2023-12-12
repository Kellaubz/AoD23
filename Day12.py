#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

## Part 1

def can_put_in(n,pos,string):
    if n+pos+2>len(string):
        return False
    if string[pos]=='#' or string[pos+n+1]=="#":
        return False
    for i in range(n):
        if string[pos+i+1]==".":
            return False
    return True

def put_in(ints,pos,string):
    return '.'+string[pos+ints[0]+2:],ints[1:]

def count_damage(ints,string):
    if len(ints)==0:
        if string.count("#")==0:
            return 1
        else:
            return 0
    else:
        s=0
        i=0
        while i<len(string) and string[i]!='#':
            if can_put_in(ints[0],i,string):
                nstring,nints=put_in(ints,i,string)
                s+=count_damage(nints,nstring)
            i+=1
        return s  

def nb_damage(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        damage='.'+lines[i].split(" ")[0]+'.'
        ints=[int(x) for x in re.findall('\d+',lines[i])]
        nb=count_damage(ints,damage)
        s+=nb
    return s
    
## Part 2  
 
def count_damage_MEM(ints,string,MEM):
    if len(ints)==0:
        if string.count("#")==0:
            return 1
        else:
            return 0
    key=(len(ints),len(string))
    if key in MEM:
        return MEM[len(ints),len(string)]
    else:
        s=0
        i=0
        while i<len(string) and string[i]!='#':
            if can_put_in(ints[0],i,string):
                nstring,nints=put_in(ints,i,string)
                s+=count_damage_MEM(nints,nstring,MEM)
            i+=1
        MEM[key]=s
        return s  

def nb_damage_time5(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        MEM={}
        line=lines[i].split(" ")[0]
        damage='.'+line+'?'+line+'?'+line+'?'+line+'?'+line+'.'
        ints=[int(x) for x in re.findall('\d+',lines[i])]
        ints=ints+ints+ints+ints+ints
        nb=count_damage_MEM(ints,damage,MEM)
        s+=nb
    return s