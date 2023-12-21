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

