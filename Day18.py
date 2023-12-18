#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

## Part 1

def is_zero(line):
    for i in range(len(line)):
        if line[i]!=0:
            return False
    return True

def dig(file):
    f=open(file,'r')
    lines=f.readlines()
    f.close()
    directions=[line.split(' ')[0] for line in lines]
    distances=[int(line.split(' ')[1]) for line in lines]
    h1,h2,v1,v2=0,0,0,0
    for i in range(len(directions)):
        if directions[i]=='R':
            h1+=distances[i]
        elif directions[i]=='L':
            h2+=distances[i]
        elif directions[i]=='D':
            v1+=distances[i]
        elif directions[i]=='U':
            v2+=distances[i]
    h=h1+h2+2
    v=v1+v2+2
    mat=[[0 for i in range(h)] for j in range(v)]
    x,y=v2+1,h2+1
    for i in range(len(directions)): # L:1, F:2, J:3, 7:4, horizontal:5, vertical:6
        if directions[i]=='R':
            if directions[i-1]=='D':
                mat[x][y]=1
            if directions[i-1]=='U':
                mat[x][y]=2
            for _ in range(distances[i]):
                y+=1
                mat[x][y]=5
        elif directions[i]=='L':
            if directions[i-1]=='D':
                mat[x][y]=3
            if directions[i-1]=='U':
                mat[x][y]=4
            for _ in range(distances[i]):
                y-=1
                mat[x][y]=5
        elif directions[i]=='D':
            if directions[i-1]=='R':
                mat[x][y]=4
            if directions[i-1]=='L':
                mat[x][y]=2
            for _ in range(distances[i]):
                x+=1
                mat[x][y]=6
        elif directions[i]=='U':
            if directions[i-1]=='R':
                mat[x][y]=3
            if directions[i-1]=='L':
                mat[x][y]=1
            for _ in range(distances[i]):
                x-=1
                mat[x][y]=6
    mat[v2+1][h2+1]=4 #input start with L and end with U
    while is_zero(mat[0]):
        mat.pop(0)
    while is_zero(mat[-1]):
        mat.pop(-1)
    while is_zero([line[0] for line in mat]):
        for line in mat:
            line.pop(0)
    while is_zero([line[-1] for line in mat]):
        for line in mat:
            line.pop(-1)
    s=0
    for i in range(len(mat)):
        cnt=0
        for j in range(len(mat[0])):
            if mat[i][j]==6:
                cnt+=1
            elif mat[i][j]==3:
                b=1
                while mat[i][j-b]==5:
                    b+=1
                if mat[i][j-b]==2:
                    cnt+=1
            elif mat[i][j]==4:
                b=1
                while mat[i][j-b]==5:
                    b+=1
                if mat[i][j-b]==1:
                    cnt+=1
            elif mat[i][j]==0:
                if cnt%2==1:
                    mat[i][j]=7
            if mat[i][j]!=0:
                s+=1
    return s

## Part 2

def dir_to_sign(int):
    if int==2 or int==1:
        return 1
    elif int==0 or int==3:
        return -1

def dig_color(file): #cut into rectangles
    f=open(file,'r')
    lines=f.readlines()
    f.close()
    directions=[int(line.split(' ')[2][-3]) for line in lines]
    distances=[int(line.split(' ')[2][2:-3],16) for line in lines]
    s=0
    h1=dir_to_sign(directions.pop(0))*distances.pop(0)
    v1=dir_to_sign(directions.pop(0))*distances.pop(0)
    while directions:
        h2=dir_to_sign(directions.pop(0))*distances.pop(0)
        v2=dir_to_sign(directions.pop(0))*distances.pop(0)
        s+=v1*h2
        if np.sign(v1)!=np.sign(v2):
            s+=min(abs(v1),abs(v2))
        if np.sign(h1)!=np.sign(h2):
            s+=min(abs(h1),abs(h2))
        h1+=h2
        v1+=v2
    return s+1
        