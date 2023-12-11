#!/usr/bin/python3
# -*- coding: utf-8 -*-

dots=['.............................................................................................................................................']
jumps=['\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n']

## Part 1

def expand(lines):    
    check_line=True
    i=0
    while i<len(lines):
        if check_line:
            j=0
            while lines[i][j]=='.':
                j+=1
            if j!=0 and lines[i][j]=='\n':
                lines=lines[:i]+dots+lines[i:]
                check_line=False
        else:
            check_line=True
        i+=1
    j=0
    while j<len(lines[0]):
        if check_line:
            i=0
            while lines[i][j]=='.':
                i+=1
            if i!=0 and lines[i][j]=='\n':
                for k in range(len(lines)):
                    lines[k]=lines[k][:j]+'.'+lines[k][j:]
                check_line=False
        else:
            check_line=True
        j+=1
    return lines

def find_galaxy(lines):
    galaxy=[]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=='#':
                galaxy+=[[i,j]]
    return galaxy

def distance_galaxy(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=lines+jumps
    lines=expand(lines)
    galaxy=find_galaxy(lines)
    s=0
    for i in range(len(galaxy)):
        for j in range(i):
            s+=abs(galaxy[i][0]-galaxy[j][0])+abs(galaxy[i][1]-galaxy[j][1])
    return s    

## Part 2

def get_emptyness(lines):
    emptyness=[[],[]]
    for i in range(len(lines)):
        j=0
        while lines[i][j]=='.':
            j+=1
        if j!=0 and lines[i][j]=='\n':
            emptyness[0].append(i)
    for j in range(len(lines[0])):
        i=0
        while lines[i][j]=='.':
            i+=1
        if i!=0 and lines[i][j]=='\n':
            emptyness[1].append(j)
    return emptyness

def older_galaxy(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=lines+jumps
    emptyness=get_emptyness(lines)
    galaxy=find_galaxy(lines)
    s=0
    for i in range(len(galaxy)):
        for j in range(i):
            a=min(galaxy[i][0],galaxy[j][0])
            b=max(galaxy[i][0],galaxy[j][0])
            c=min(galaxy[i][1],galaxy[j][1])
            d=max(galaxy[i][1],galaxy[j][1])
            h=0
            v=0
            for k in range(a,b+1):
                if k in emptyness[0]:
                    h+=1
            for k in range(c,d+1):
                if k in emptyness[1]:
                    v+=1
            s+=999999*(h+v)+b+d-a-c
    return s

