#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_not_null(L):
    for l in L:
        if l!=0:
            return True
    return False

def next_diff(L):
    return [L[i+1]-L[i] for i in range(len(L)-1)]

## Part 1

def oasis_prediction(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    prediction=[]
    for i in range(len(lines)):
        lines[i]=[[int(l) for l in lines[i][:-1].split(' ')]]
    for i in range(len(lines)):
        diff=lines[i][0]
        while is_not_null(diff):
            diff=next_diff(diff)
            lines[i].append(diff)
        p=0
        for j in range(len(lines[i])):
            p+=lines[i][j][-1]
        prediction.append(p)
    return sum(prediction)
    
## Part 2

def oasis_backward(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    prediction=[]
    for i in range(len(lines)):
        lines[i]=[[int(l) for l in lines[i][:-1].split(' ')]]
    for i in range(len(lines)):
        diff=lines[i][0]
        while is_not_null(diff):
            diff=next_diff(diff)
            lines[i].append(diff)
        p=0
        for j in range(len(lines[i])):
            p+= (-1)**j*lines[i][j][0]
        prediction.append(p)
    return sum(prediction)
 