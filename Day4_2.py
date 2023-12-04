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

def scratch_cards(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    nb_sc=[1 for i in range(len(lines))]
    for i in range(len(lines)):
        win,got=get_number(lines[i])
        cnt=0
        for j in range(len(got)):
            if got[j] in win:
                cnt=cnt+1
        for j in range(cnt):
            try :
                nb_sc[i+j+1]=nb_sc[i+j+1]+nb_sc[i]
            except IndexError:
                pass
    s=sum(nb_sc)
    return s
    