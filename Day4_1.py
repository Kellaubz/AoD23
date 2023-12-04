#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

nb_wn=10

def get_number(string):
    tmp=re.findall('\d+',string)
    for i in range(len(tmp)):
        tmp[i]=int(tmp[i])
    win=tmp[1:nb_wn+1]
    got=tmp[nb_wn+1:]
    return (win,got)    

def colorful_cards(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        win,got=get_number(lines[i])
        cnt=-1
        for i in range(len(got)):
            if got[i] in win:
                cnt=cnt+1
        if cnt>=0:
            s=s+2**cnt
    return s
    