#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def init_list_bricks(lines):
    bricks = []
    max_height = 0
    for line in lines:
        [bot,top] = line[:-1].split('~')
        [a,b,c] = bot.split(',')
        a,b,c = int(a),int(b),int(c)
        [x,y,z] = top.split(',')
        x,y,z = int(x),int(y),int(z)
        length = 0
        kind = 0
        under = set([]) # set of bricks under this brick
        over = set([]) # set of bricks over this brick
        stable = False
        if c == z:
            if b == y:
                length = x - a + 1
            else:
                length = y - b + 1
                kind = 1
        else:
            length = z - c + 1
            kind = 2
        bricks.append([a,b,c,x,y,z,length,kind,under,over,stable])
        if z > max_height:
            max_height = z
    return bricks,max_height

def init_support(bricks,i):
    base_height = bricks[i][2]
    if base_height == 1:
        bricks[i][10] = True
    else:
        for j in range(len(bricks)):
            if bricks[j][5] == base_height - 1:
                if bricks[j][0] <= bricks[i][0] <= bricks[j][3] or bricks[i][0] <= bricks[j][0] <= bricks[i][3]:
                    if bricks[j][1] <= bricks[i][1] <= bricks[j][4] or bricks[i][1] <= bricks[j][1] <= bricks[i][4]:
                        bricks[i][8].add(j)
                        bricks[j][9].add(i)
                        if bricks[j][10]:
                            bricks[i][10] = True

def fall(bricks,i):
    if not(bricks[i][10]) and len(bricks[i][8]) == 0:
        bricks[i][2] -= 1
        bricks[i][5] -= 1
        for j in bricks[i][9]:
            bricks[j][8].remove(i)
        bricks[i][9] = set([])
        init_support(bricks,i)
        return True
    return False

def can_disintegrate(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    bricks,max_height = init_list_bricks(lines)
    for h in range(1,max_height+1):
        for i in range(len(bricks)):
            if bricks[i][2] == h:
                init_support(bricks,i)
    at_least_one_fall = True
    while at_least_one_fall:
        at_least_one_fall = False
        for h in range(2,max_height+1):
            for i in range(len(bricks)):
                if bricks[i][5] == h:
                    if fall(bricks,i):
                        at_least_one_fall = True
    cnt_can_disintegrate = 0
    for i in range(len(bricks)):
        for j in bricks[i][9]:
            if len(bricks[j][8]) == 1:
                break
        else: # no break
            cnt_can_disintegrate += 1
    return cnt_can_disintegrate

## Part 2

def set_stable(bricks):
    for i in range(len(bricks)):
        bricks[i][10] = True

def count_unstable(bricks):
    cnt_unstable = 0
    for i in range(len(bricks)):
        if not(bricks[i][10]):
            cnt_unstable += 1
    return cnt_unstable

def nb_other_fall(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    bricks,max_height = init_list_bricks(lines)
    for h in range(1,max_height+1):
        for i in range(len(bricks)):
            if bricks[i][2] == h:
                init_support(bricks,i)
    at_least_one_fall = True
    while at_least_one_fall:
        at_least_one_fall = False
        for h in range(2,max_height+1):
            for i in range(len(bricks)):
                if bricks[i][5] == h:
                    if fall(bricks,i):
                        at_least_one_fall = True
    other_fall = {}
    for h in range(max_height):
        for i in range(len(bricks)):
            if bricks[i][5] == max_height - h:
                other_fall[i] = 0
                bricks[i][10] = False
                to_process = [i]
                while to_process:
                    current = to_process.pop(0)
                    for j in bricks[current][8]:
                        if bricks[j][10]:
                            break
                    else: # no break
                        if bricks[current][10]:
                            other_fall[i] += 1
                        bricks[current][10] = False
                    if not(bricks[current][10]):
                        for j in bricks[current][9]:
                            if bricks[j][10]:
                                if j not in to_process:
                                    to_process.append(j)
                set_stable(bricks)
    s = 0
    for i in other_fall:
        s += other_fall[i]
    return s


