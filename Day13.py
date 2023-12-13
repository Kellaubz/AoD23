#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def find_h_cut(block):
    n=len(block)
    for i in range(1,n):
        m=min(i,n-i)
        b1=[]
        b2=[]
        for j in range(m):
            b1.append(block[i-j-1])
            b2.append(block[i+j])
        if b1==b2:
            return i
    return None

def find_v_cut(block):
    n=len(block[0])
    c_block=block
    c_block=[list(line) for line in c_block]
    trans_block=[[c_block[j][i] for j in range(len(c_block))] for i in range(len(c_block[0]))]
    return find_h_cut(trans_block)
    
def reflexion(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    blocks=[]
    b=[]
    for line in lines:
        if line!="\n":
            b.append(line[:-1])
        else:
            blocks.append(b)
            b=[]
    blocks.append(b)
    s=0
    for block in blocks:
        nb=0
        h=find_h_cut(block)
        if h != None:
            nb+=100*h
        else :
            v=find_v_cut(block)
            if v != None:
                nb+=v
            else:
                pass
                print(block)
                raise Exception("No cut found")
        s+=nb
    return s

## Part 2

def smudge(b1,b2):
    n=0
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b1[i][j]!=b2[i][j]:
                n+=1
    return n

def smudge_find_h_cut(block):
    n=len(block)
    for i in range(1,n):
        m=min(i,n-i)
        b1=[]
        b2=[]
        for j in range(m):
            b1.append(block[i-j-1])
            b2.append(block[i+j])
        if smudge(b1,b2)==1:
            return i
    return None

def smudge_find_v_cut(block):
    n=len(block[0])
    c_block=block
    c_block=[list(line) for line in c_block]
    trans_block=[[c_block[j][i] for j in range(len(c_block))] for i in range(len(c_block[0]))]
    return smudge_find_h_cut(trans_block)

def smudge_reflexion(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    blocks=[]
    b=[]
    for line in lines:
        if line!="\n":
            b.append(line[:-1])
        else:
            blocks.append(b)
            b=[]
    blocks.append(b)
    s=0
    for block in blocks:
        nb=0
        h=smudge_find_h_cut(block)
        if h != None:
            nb+=100*h
        else :
            v=smudge_find_v_cut(block)
            if v != None:
                nb+=v
            else:
                raise Exception("No cut found")
        s+=nb
    return s
