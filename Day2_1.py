#!/usr/bin/python3
# -*- coding: utf-8 -*-

rgb=['red','green','blue']
game_number=[12,13,14]

def color_number(string):
    for i in range(len(rgb)):
        if string[0:len(rgb[i])]==rgb[i]:
            return i
    raise ValueError("Color not found")
    
def comp_list(list1,list2):
    for i in range(len(list1)):
        if list1[i]>list2[i]:
            return True
    return False

def color_game(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        line=lines[i].split(":")[1]
        sets=line.split(";")
        booly=True
        for j in range(len(sets)):
            sets[j]=sets[j].split(",")
            colors=[0,0,0]
            for k in range(len(sets[j])):
                sets[j][k]=sets[j][k].split(" ")
                colors[color_number(sets[j][k][2])]=int(sets[j][k][1])
            if comp_list(colors,game_number):
                booly=False
                break
        if booly:
            s=s+i+1
    return s
    