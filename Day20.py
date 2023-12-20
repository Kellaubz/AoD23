#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def init_dico(lines):
    dico = {}
    for line in lines:
        v = [0,[],{},0] # [type, [outputs], last_signal_received, on/off]
        line = line[:-1].split('->')
        key = line[0][:-1]
        if line[0][0] == '%': # Flip-flop stocked as 1
            v[0] = 1
            key = line[0][1:-1]
        elif line[0][0] == '&': # Conjunction stocked as 2
            v[0] = 2
            key = line[0][1:-1]
        for l in line[1].split(','):
            v[1].append(l[1:])
        dico[key] = v
    for key in dico:
        for o in dico[key][1]:
            if o in dico:
                if dico[o][0] == 2:
                    dico[o][2][key] = 0
    return dico

def count_pulse(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    dico = init_dico(lines)
    signals = [0,0] # [low,high]
    for _ in range(1000):
        to_process = [['broadcaster',0,'button']] # [key,signal,source]
        while to_process:
            [key,signal,source] = to_process.pop(0)
            signals[signal] += 1
            if not key in dico:
                continue
            module = dico[key]
            if module[0] == 0: # Broadcaster
                for o in module[1]:
                    to_process.append([o,0,key])
            elif module[0] == 1: # Flip-flop
                if signal == 0:
                    new_signal = 0
                    if module[3] == 0:
                        new_signal = 1
                        module[3] = 1
                    else: 
                        module[3] = 0
                    for o in module[1]:
                        to_process.append([o,new_signal,key])
            elif module[0] == 2: # Conjunction
                module[2][source] = signal
                all_high=True
                for o in module[2]:
                    if module[2][o] == 0:
                        all_high = False
                        break
                new_signal = 1
                if all_high:
                    new_signal = 0
                for o in module[1]:
                    to_process.append([o,new_signal,key])
    return signals[0]*signals[1]

## Part 2 

################################################################
#                                                              #
#  At the end of the day, it was faster by hand than by code.  #
#                                                              #
################################################################
