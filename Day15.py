#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def hash_block(line):
    n=len(line)
    h=0
    for i in range(n):
        h+=ord(line[i])
        h*=17
        h=h%256
    return h

def hash_file(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[line[:-1].split(',') for line in lines]
    s=0
    for l in lines[0]:
        s+=hash_block(l)
    return s

## Part 2

def Holiday_ASCII(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[line[:-1].split(',') for line in lines]
    line=lines[0]
    line=[l.split('=') for l in line]
    for i in range(len(line)):
        if len(line[i])==1:
            line[i]=[line[i][0][:-1],'-']
    Hash_Table={}
    for l in line:
        if not(l[0] in Hash_Table):
            Hash_Table[l[0]]=hash_block(l[0])
    for i in range(len(line)):
        if line[i][1]!='-':
            line[i][1]=int(line[i][1])
    blocks=[[] for i in range(256)]
    for l in line:
        k=Hash_Table[l[0]]
        if l[1]=='-':
            for i in range(len(blocks[k])):
                if blocks[k][i][0]==l[0]:
                    blocks[k].pop(i)
                    break
        else:
            putit=True
            for i in range(len(blocks[k])):
                if blocks[k][i][0]==l[0]:
                    blocks[k][i][1]=l[1]
                    putit=False
            if putit:
                blocks[k].append(l)
    s=0
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            nb=blocks[i][j][1]*(i+1)*(j+1)
            s+=nb
    return s
        
