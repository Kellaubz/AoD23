#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def is_valid_path(d,c):
    if c == '#':
        return False
    if c == '.':
        return True
    if c == '>':
        return d == (0,1)
    if c == '<':
        return d == (0,-1)
    if c == '^':
        return d == (-1,0)
    if c == 'v':
        return d == (1,0)

def init_paths(lines,start,end):
    paths = {}
    starts = [start]
    while starts:
        (s,dir) = starts.pop(0)
        first_pos = s
        first_dir = dir
        length_path = 0
        follow_path = True
        next_dir = [dir]
        while follow_path:
            length_path += 1
            dir = next_dir[0]
            next_dir = []
            s = (s[0]+dir[0],s[1]+dir[1])
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                if d != (-dir[0],-dir[1]):
                    if is_valid_path(d,lines[s[0]+d[0]][s[1]+d[1]]) :
                        next_dir.append(d)
            if len(next_dir) == 0:
                #print("End of path")
                follow_path = False
                if s == end:
                    paths[(first_pos,first_dir)] = [length_path,s]
            elif len(next_dir) >= 2:
                #print("Split path")
                for d in next_dir:
                    if (s,d) not in paths:
                        starts.append((s,d))
                follow_path = False
                paths[(first_pos,first_dir)] = [length_path,s]
    return paths
            
def long_hike(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = ['#'] + list(lines[i][:-1]) + ['#']
    lines = [['#']*(len(lines[0]))] + lines + [['#']*(len(lines[0]))]
    s = (0,0)
    for j in range(len(lines[1])):
        if lines[1][j] == '.':
            s = (1,j)
            break
    if s == (0,0):
        raise ValueError("No start found")
    end = (0,0)
    for j in range(len(lines[-2])):
        if lines[-2][j] == '.':
            end = (len(lines)-2,j)
            break
    if end == (0,0):
        raise ValueError("No end found")
    start = (s,(1,0))
    paths = init_paths(lines,start,end)
    ongoing_hikes = [[start,[],0]] # (pos,keys,steps)
    finished_hikes = []
    while ongoing_hikes:
        (pos,keys,steps) = ongoing_hikes.pop(0)
        keys = keys*1
        if pos in paths:
            steps += paths[pos][0]
            keys.append(pos[0])
            next_pos = paths[pos][1]
            if next_pos == end:
                finished_hikes.append((keys,steps))
            elif not next_pos in keys:
                for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if (next_pos,d) in paths:
                        ongoing_hikes.append(((next_pos,d),keys,steps))
    steps = [h[1] for h in finished_hikes]
    return max(steps)

## Part 2

def is_valid_path2(d,c):
    if c == '#':
        return False
    else :
        return True

def init_paths2(lines,start,end):    
    paths = {}
    starts = [start]
    while starts:
        (s,dir) = starts.pop(0)
        first_pos = s
        first_dir = dir
        length_path = 0
        follow_path = True
        next_dir = [dir]
        while follow_path:
            length_path += 1
            dir = next_dir[0]
            next_dir = []
            s = (s[0]+dir[0],s[1]+dir[1])
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                if d != (-dir[0],-dir[1]):
                    if is_valid_path2(d,lines[s[0]+d[0]][s[1]+d[1]]) :
                        next_dir.append(d)
            if len(next_dir) == 0:
                #print("End of path")
                follow_path = False
                if s == end:
                    paths[(first_pos,first_dir)] = [length_path,s]
            elif len(next_dir) >= 2:
                #print("Split path")
                for d in next_dir:
                    if (s,d) not in paths:
                        starts.append((s,d))
                follow_path = False
                paths[(first_pos,first_dir)] = [length_path,s]
    return paths

def long_hike2(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = ['#'] + list(lines[i][:-1]) + ['#']
    lines = [['#']*(len(lines[0]))] + lines + [['#']*(len(lines[0]))]
    s = (0,0)
    for j in range(len(lines[1])):
        if lines[1][j] == '.':
            s = (1,j)
            break
    if s == (0,0):
        raise ValueError("No start found")
    end = (0,0)
    for j in range(len(lines[-2])):
        if lines[-2][j] == '.':
            end = (len(lines)-2,j)
            break
    if end == (0,0):
        raise ValueError("No end found")
    start = (s,(1,0))
    paths = init_paths2(lines,start,end)
    ongoing_hikes = [[start,[],0]] # (pos,keys,steps)
    finished_hikes = []
    max_steps = 0
    while ongoing_hikes:
        #print(len(ongoing_hikes))   
        hike = ongoing_hikes.pop()
        (pos,keys,steps) = hike
        keys = keys*1
        steps += paths[pos][0]
        keys.append(pos[0])
        next_pos = paths[pos][1]
        if next_pos == end:
            if steps > max_steps:
                max_steps = steps
                print(max_steps) # well, it is a bit slow to run so I tried this so it show the step by step results. This solution is a bit shady, but it does work ;)
            finished_hikes.append((keys,steps))
        elif not next_pos in keys:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                if (next_pos,d) in paths:
                    ongoing_hikes.append(((next_pos,d),keys,steps))
    steps = [h[1] for h in finished_hikes]
    return max(steps)



        