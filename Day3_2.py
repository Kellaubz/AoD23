#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

dots='...........................................................................................................................................................'

def get_number(string):
    res=[]
    if string[3].isdigit():
        if not(string[4].isdigit()):
            res.append(int(re.findall('\d+',string[1:4])[-1]))
        elif not(string[2].isdigit()):
            res.append(int(re.findall('\d+',string[3:6])[0]))
        else:
            res.append(int(re.findall('\d+',string[2:5])[0]))
    else:
        if string[4].isdigit():
            res.append(int(re.findall('\d+',string[4:])[0]))
        if string[2].isdigit():
            res.append(int(re.findall('\d+',string[:3])[-1]))
    return res
    


def nb_around(i,j,lines):
    top=lines[i-1][j-3:j+4]
    tn=get_number(top)
    bot=lines[i+1][j-3:j+4]
    bn=get_number(bot)
    mid=lines[i][j-3:j+4]
    mn=get_number(mid)
    return tn+bn+mn

def go_faster(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[dots]+lines+[dots]
    for i in range(len(lines)):
        lines[i]='...'+lines[i][:-1]+'....'
    s=0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=='*':
                ar=nb_around(i,j,lines)
                if len(ar)==2:
                    power=ar[0]*ar[1]
                    s=s+power
    return s
    