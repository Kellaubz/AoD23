#!/usr/bin/python3
# -*- coding: utf-8 -*-

rgb=['red','green','blue']
game_number=[12,13,14]

def color_number(string):
    for i in range(len(rgb)):
        if string[0:len(rgb[i])]==rgb[i]:
            return i
    raise ValueError("Color not found")

def list_to_rgb(list):
    a,b,c=[],[],[]
    for l in list:
        a.append(l[0])
        b.append(l[1])
        c.append(l[2])
    return a,b,c

def power_color_game(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        line=lines[i].split(":")[1]
        sets=line.split(";")
        colors=[]
        for j in range(len(sets)):
            sets[j]=sets[j].split(",")
            colors.append([0,0,0])
            for k in range(len(sets[j])):
                sets[j][k]=sets[j][k].split(" ")
                colors[j][color_number(sets[j][k][2])]=int(sets[j][k][1])
        red,green,blue=list_to_rgb(colors)
        minlist=[max(red),max(green),max(blue)]
        power=minlist[0]*minlist[1]*minlist[2]
        print(i+1)
        print(power)
        s=s+power
    return s
    