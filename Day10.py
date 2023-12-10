#!/usr/bin/python3
# -*- coding: utf-8 -*-

dots=['....................................................................................................................................']

## Part 1

def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=='S':
                return [i,j]
    raise Exception("No start found")

def next_pos_start(lines,start): #1:up,2:right,3:down,4:left
    [i,j]=start
    if lines[i-1][j]=='7' or lines[i-1][j]=='F' or lines[i-1][j]=='|':
        return [i-1,j,3]
    elif lines[i][j+1]=='7' or lines[i][j+1]=='J' or lines[i][j+1]=='-':
        return [i,j+1,4]
    elif lines[i+1][j]=='L' or lines[i+1][j]=='J' or lines[i+1][j]=='|':
        return [i+1,j,1]
    elif lines[i][j-1]=='L' or lines[i][j-1]=='F' or lines[i][j-1]=='-':
        return [i,j-1,2]
    raise Exception("No next position found")

def next_pos(lines,pos): #from 1:up,2:right,3:down,4:left
    [i,j,d]=pos
    s=lines[i][j]
    if s=='7':
        if d==3:
            return [i,j-1,2]
        elif d==4:
            return [i+1,j,1]
        else:
            raise Exception("No next position found")
    elif s=='L':
        if d==1:
            return [i,j+1,4]
        elif d==2:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='F':
        if d==3:
            return [i,j+1,4]
        elif d==2:
            return [i+1,j,1]
        else:
            raise Exception("No next position found")
    elif s=='J':
        if d==1:
            return [i,j-1,2]
        elif d==4:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='|':
        if d==1:
            return [i+1,j,1]
        elif d==3:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='-':
        if d==2:
            return [i,j-1,2]
        elif d==4:
            return [i,j+1,4]
        else:
            raise Exception("No next position found")

def size_loop(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=dots+lines+dots
    for i in range(len(lines)):
        lines[i]='.'+lines[i][:-1]+'.'
    start=find_start(lines)
    pos=next_pos_start(lines,start)
    s=1
    while pos[:2]!=start:
        s+=1
        pos=next_pos(lines,pos)
    return s//2

## Part 2

def next_pos_mod(lines,pos): #from 1:up,2:right,3:down,4:left
    [i,j,d]=pos
    s=lines[i][j]
    lines[i][j]=s+'!'
    if s=='7':
        if d==3:
            return [i,j-1,2]
        elif d==4:
            return [i+1,j,1]
        else:
            raise Exception("No next position found")
    elif s=='L':
        if d==1:
            return [i,j+1,4]
        elif d==2:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='F':
        if d==3:
            return [i,j+1,4]
        elif d==2:
            return [i+1,j,1]
        else:
            raise Exception("No next position found")
    elif s=='J':
        if d==1:
            return [i,j-1,2]
        elif d==4:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='|':
        if d==1:
            return [i+1,j,1]
        elif d==3:
            return [i-1,j,3]
        else:
            raise Exception("No next position found")
    elif s=='-':
        if d==2:
            return [i,j-1,2]
        elif d==4:
            return [i,j+1,4]
        else:
            raise Exception("No next position found")

def area_loop(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=dots+lines+dots
    for i in range(len(lines)):
        lines[i]='.'+lines[i][:-1]+'.'
    for i in range(len(lines)):
        lines[i]=list(lines[i])
    start=find_start(lines)
    lines[start[0]][start[1]]='S!'
    pos=next_pos_start(lines,start)
    while pos[:2]!=start:
        pos=next_pos_mod(lines,pos)
    a=0
    for i in range(len(lines)):
        b=1
        for j in range(len(lines[i])):
            if lines[i][j]=='|!':
                b+=1
            elif lines[i][j]=='J!' :
                c=1
                while lines[i][j-c]=='-!':
                    c+=1
                if lines[i][j-c]=='F!':
                    b+=1
            elif lines[i][j]=='7!':
                c=1
                while lines[i][j-c]=='-!':
                    c+=1
                if lines[i][j-c]=='L!':
                    b+=1
            elif b//2==b/2 and len(lines[i][j])!=2:
                a+=1
    return a
