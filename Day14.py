#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def tilt_north(lines):
    copy=[line[:] for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if copy[i][j]=="O":
                k=i
                while k>0 and copy[k-1][j]==".":
                    copy[k-1][j]="O"
                    copy[k][j]="."
                    k-=1
    return copy

def count_load(lines):
    n=len(lines)
    s=0
    for i in range(n):
        for c in lines[i]:
            if c=="O":
                s+=n-i
    return s

def north_load(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[list(line[:-1]) for line in lines]
    lines=tilt_north(lines)
    return count_load(lines)

## Part 2

cyc=34 # because I'm a magician, I know that the period of the periodic phase of my input is 34

def transpose(lines):
    n,m=len(lines),len(lines[0])
    lines=[[lines[i][j] for i in range(n)] for j in range(m)]
    return lines

def turn_south(lines):
    n,m=len(lines),len(lines[0])
    lines=[[lines[-i-1][j] for j in range(m)] for i in range(n)]
    return lines

def tilt_west(lines):
    lines=transpose(lines)
    lines=tilt_north(lines)
    lines=transpose(lines)
    return lines

def tilt_east(lines):
    lines=transpose(lines)
    lines=turn_south(lines)
    lines=tilt_north(lines)
    lines=turn_south(lines)
    lines=transpose(lines)
    return lines

def tilt_south(lines):
    lines=turn_south(lines)
    lines=tilt_north(lines)
    lines=turn_south(lines)
    return lines

def cycle(lines):
    lines=tilt_north(lines)
    lines=tilt_west(lines)
    lines=tilt_south(lines)
    lines=tilt_east(lines)
    return lines

def count_cycle_load(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[list(line[:-1]) for line in lines]
    copy1=[line[:] for line in lines]
    copy2=cycle(copy1)
    while lines!=copy2:
        lines=[line[:] for line in copy2]
        for _ in range(cyc):
            copy1=[line[:] for line in copy2]
            copy2=cycle(copy1)
    cyc_left=10**9%34-1
    for _ in range(cyc_left):
        copy1=[line[:] for line in copy2]
        copy2=cycle(copy1)
    return count_load(copy2)

    
    