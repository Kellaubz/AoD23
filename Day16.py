#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

diese=[['#'] for i in range(113)]

def move(beam,char):
    if char=='.':
        return [[[beam[0][0]+beam[1][0],beam[0][1]+beam[1][1]],beam[1]]]
    elif char=='/':
        if beam[1]==[1,0]:
            dir=[0,-1]
            pos=[beam[0][0],beam[0][1]-1]
            return [[pos,dir]]
        elif beam[1]==[0,-1]:
            dir=[1,0]
            pos=[beam[0][0]+1,beam[0][1]]
            return [[pos,dir]]
        elif beam[1]==[-1,0]:
            dir=[0,1]
            pos=[beam[0][0],beam[0][1]+1]
            return [[pos,dir]]
        elif beam[1]==[0,1]:
            dir=[-1,0]
            pos=[beam[0][0]-1,beam[0][1]]
            return [[pos,dir]]
    elif char=='\\':
        if beam[1]==[1,0]:
            dir=[0,1]
            pos=[beam[0][0],beam[0][1]+1]
            return [[pos,dir]]
        elif beam[1]==[0,-1]:
            dir=[-1,0]
            pos=[beam[0][0]-1,beam[0][1]]
            return [[pos,dir]]
        elif beam[1]==[-1,0]:
            dir=[0,-1]
            pos=[beam[0][0],beam[0][1]-1]
            return [[pos,dir]]
        elif beam[1]==[0,1]:
            dir=[1,0]
            pos=[beam[0][0]+1,beam[0][1]]
            return [[pos,dir]]
    elif char=='-':
        if beam[1]==[1,0] or beam[1]==[-1,0]:
            dir1=[0,1]
            dir2=[0,-1]
            pos1=[beam[0][0],beam[0][1]+1]
            pos2=[beam[0][0],beam[0][1]-1]
            return [[pos1,dir1],[pos2,dir2]]
        elif beam[1]==[0,-1] or beam[1]==[0,1]:
            dir=beam[1]
            pos=[beam[0][0]+dir[0],beam[0][1]+dir[1]]
            return [[pos,dir]]
    elif char=='|':
        if beam[1]==[1,0] or beam[1]==[-1,0]:
            dir=beam[1]
            pos=[beam[0][0]+dir[0],beam[0][1]+dir[1]]
            return [[pos,dir]]
        elif beam[1]==[0,-1] or beam[1]==[0,1]:
            dir1=[1,0]
            dir2=[-1,0]
            pos1=[beam[0][0]+1,beam[0][1]]
            pos2=[beam[0][0]-1,beam[0][1]]
            return [[pos1,dir1],[pos2,dir2]]       

def print_beam(energy_map):
    str=''
    for i in range(1,len(energy_map)-1):
        for j in range(1,len(energy_map[1])-1):
            str+='.'*(len(energy_map[i][j])==0)+'#'*(len(energy_map[i][j])!=0)
            #s+=(len(energy_map[i][j])!=0)
        str+='\n'
    print(str)


def laser(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[['#']+list(line[:-1])+['#'] for line in lines]
    lines=[diese]+lines+[diese]
    n=len(lines)
    m=len(lines[1])
    energy_map=[[[] for _ in range(m)] for _ in range(n)]
    beams=[[[1,1],[0,1]]]
    to_rm=[]
    while beams!=[]:
        #print_beam(energy_map)
        for i in range(len(beams)):
            char=lines[beams[i][0][0]][beams[i][0][1]][0]
            if char=='#':
                to_rm.append(i)
            elif beams[i][1] in energy_map[beams[i][0][0]][beams[i][0][1]]:
                to_rm.append(i)
            else:
                energy_map[beams[i][0][0]][beams[i][0][1]].append(beams[i][1])
                tmp=move(beams[i],char)
                if tmp!=None:
                    beams[i]=tmp[0]
                    for e in tmp[1:]:
                        beams.append(e)
        to_rm.sort(reverse=True)
        for i in to_rm:
            beams.pop(i)
        to_rm=[]
    s=0
    for i in range(1,len(energy_map)-1):
        for j in range(1,len(energy_map[1])-1):
            s+=(len(energy_map[i][j])!=0)
    return s

## Part 2

def count_energy(init_beam,lines):
    n=len(lines)
    m=len(lines[1])
    beams=[init_beam]
    energy_map=[[[] for _ in range(m)] for _ in range(n)]
    to_rm=[]
    while beams!=[]:
        for i in range(len(beams)):
            char=lines[beams[i][0][0]][beams[i][0][1]][0]
            if char=='#':
                to_rm.append(i)
            elif beams[i][1] in energy_map[beams[i][0][0]][beams[i][0][1]]:
                to_rm.append(i)
            else:
                energy_map[beams[i][0][0]][beams[i][0][1]].append(beams[i][1])
                tmp=move(beams[i],char)
                if tmp!=None:
                    beams[i]=tmp[0]
                    for e in tmp[1:]:
                        beams.append(e)
        to_rm.sort(reverse=True)
        for i in to_rm:
            beams.pop(i)
        to_rm=[]
    s=0
    for i in range(1,len(energy_map)-1):
        for j in range(1,len(energy_map[1])-1):
            s+=(len(energy_map[i][j])!=0)
    return s
 
def max_laser(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    lines=[['#']+list(line[:-1])+['#'] for line in lines]
    lines=[diese]+lines+[diese]
    n=len(lines)
    m=len(lines[1])
    border_beams=[[[1,i],[1,0]] for i in range(1,m-1)]+[[[i,1],[0,1]] for i in range(1,n-1)]+[[[n-2,i],[-1,0]] for i in range(1,m-1)]+[[[i,m-2],[0,-1]] for i in range(1,n-1)]
    s=0
    for beam in border_beams:
        s=max(s,count_energy(beam,lines))
    return s