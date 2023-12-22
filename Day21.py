#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

D=['#' for _ in range(133)] # 133 is the length of a line + 2

def reset_buffer(buffer):
    for i in range(len(buffer)):
        for j in range(len(buffer[i])):
            buffer[i][j] = False

def print_lines(lines):
    for line in lines:
        string = ''
        for c in line:
            string += c
        print(string)

def step_64(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = ['#']+list(lines[i][:-1])+['#']
    lines = [D]+lines+[D]
    buffer = [[False for _ in range(len(lines[i]))] for i in range(len(lines))]
    start=[0,0]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start = [i,j]
                break
        else: # if not break (this use the structure for-else)
            continue
        break
    lines[start[0]][start[1]] = '!'
    for _ in range(64):
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '!':
                    buffer[i+1][j] = not lines[i+1][j] == '#'
                    buffer[i-1][j] = not lines[i-1][j] == '#'
                    buffer[i][j+1] = not lines[i][j+1] == '#'
                    buffer[i][j-1] = not lines[i][j-1] == '#'
                    lines[i][j] = '.'
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if buffer[i][j]:
                    lines[i][j] = '!'
        reset_buffer(buffer)
    count = 0
    #print_lines(lines)
    for line in lines:
        for c in line:
            if c == '!':
                count += 1
    return count

## Part 2

# My input does not satisfy the conditions to have a "quadratic polynomial" solution.

nb_of_steps = 26501365

def count(lines,steps,start):
    buffer = [[False for _ in range(len(lines[i]))] for i in range(len(lines))]
    if start != None:
        if lines[start[0]][start[1]] == '#':
            raise ValueError('Start point is a rock')
        lines[start[0]][start[1]] = '!'
    for _ in range(steps):
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '!':
                    buffer[i+1][j] = not lines[i+1][j] == '#'
                    buffer[i-1][j] = not lines[i-1][j] == '#'
                    buffer[i][j+1] = not lines[i][j+1] == '#'
                    buffer[i][j-1] = not lines[i][j-1] == '#'
                    lines[i][j] = '.'
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if buffer[i][j]:
                    lines[i][j] = '!'
        reset_buffer(buffer)
    count = 0
    #print_lines(lines)
    for line in lines:
        for c in line:
            if c == '!':
                count += 1
    reset_grid(lines)
    return count

def reset_grid(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '!':
                lines[i][j] = '.'

def count_step_torus(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = ['#'] + list(lines[i][:-1]) + ['#']
    lines = [D] + lines + [D]
    n = len(lines)
    lines[n//2][n//2] = '.'
    mid = [n//2,n//2]
    north = [1,n//2]
    south = [n-2,n//2]
    west = [n//2,1]
    east = [n//2,n-2]
    nw = [1,1]
    ne = [1,n-2]
    sw = [n-2,1]
    se = [n-2,n-2]
    small_diag = (nb_of_steps - 1) % (n-2) 
    big_diag = 2*(n-2) - small_diag - 3 # careful counting
    nb_full_odd_pos = count(lines,n,mid)
    nb_full_even_pos = count(lines,n+1,mid)
    # print(nb_full_odd_pos,nb_full_even_pos)
    # nb_full_odd_pos = 7744
    # nb_full_even_pos = 7806
    radius = nb_of_steps//(n-2)
    rest = (nb_of_steps - (n-2)//2-1) % (n-2) 
    nb_full_odd_grid = 1 # the middle grid is odd
    nb_full_even_grid = 0
    for i in range(radius):
        if i%2 == 0:
            nb_full_odd_grid += 4*i # the first grid is odd
        else:
            nb_full_even_grid += 4*i
    total_full_grid = nb_full_odd_pos*nb_full_odd_grid + nb_full_even_pos*nb_full_even_grid
    nb_north_pos = count(lines,rest,north)
    nb_south_pos = count(lines,rest,south)
    nb_west_pos = count(lines,rest,west)
    nb_east_pos = count(lines,rest,east)
    # print(nb_north_pos,nb_south_pos,nb_west_pos,nb_east_pos)
    # nb_north_pos = 5852
    # nb_south_pos = 5839
    # nb_west_pos = 5842
    # nb_east_pos = 5849
    nb_nw_small_diag_pos = count(lines,small_diag,nw)
    nb_ne_small_diag_pos = count(lines,small_diag,ne)
    nb_sw_small_diag_pos = count(lines,small_diag,sw)
    nb_se_small_diag_pos = count(lines,small_diag,se)
    # print(nb_nw_small_diag_pos,nb_ne_small_diag_pos,nb_sw_small_diag_pos,nb_se_small_diag_pos)
    # nb_nw_small_diag_pos = 999
    # nb_ne_small_diag_pos = 1000
    # nb_sw_small_diag_pos = 984
    # nb_se_small_diag_pos = 982
    nb_nw_big_diag_pos = count(lines,big_diag,nw)
    nb_ne_big_diag_pos = count(lines,big_diag,ne)
    nb_sw_big_diag_pos = count(lines,big_diag,sw)
    nb_se_big_diag_pos = count(lines,big_diag,se)
    # print(nb_nw_big_diag_pos,nb_ne_big_diag_pos,nb_sw_big_diag_pos,nb_se_big_diag_pos)
    # nb_nw_big_diag_pos = 6799
    # nb_ne_big_diag_pos = 6797
    # nb_sw_big_diag_pos = 6787
    # nb_se_big_diag_pos = 6796
    total_vertex_diamond = nb_north_pos + nb_south_pos + nb_west_pos + nb_east_pos
    total_small_diag = (nb_nw_small_diag_pos + nb_ne_small_diag_pos + nb_sw_small_diag_pos + nb_se_small_diag_pos)*radius
    total_big_diag = (nb_nw_big_diag_pos + nb_ne_big_diag_pos + nb_sw_big_diag_pos + nb_se_big_diag_pos)*(radius-1)
    total = total_full_grid + total_small_diag + total_big_diag + total_vertex_diamond 
    # print(total_full_grid,total_small_diag,total_big_diag,total_vertex_diamond)
    return total