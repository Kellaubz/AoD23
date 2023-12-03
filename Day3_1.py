#!/usr/bin/python3
# -*- coding: utf-8 -*-

dots='...........................................................................................................................................................'

def is_not_dots(string):
    return string!=dots[:len(string)]

def get_number(i,j,dglen,lines):
    return int(lines[i][j-dglen:j])

def lookaround(i,j,dglen,lines):
    copy=[dots]+lines+[dots]
    for k in range(len(copy)):
        copy[k]='.'+copy[k][:-1]+'..'
    around=[copy[i][j-dglen:j+2],copy[i+1][j-dglen],copy[i+1][j+1],copy[i+2][j-dglen:j+2]]
    for l in around:
        if is_not_dots(l):
            return True
    return False


def gondola(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for i in range(len(lines)):
        dglen=0
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                dglen=dglen+1
            else:
                if dglen>0:
                    if lookaround(i,j,dglen,lines):
                        s=get_number(i,j,dglen,lines)+s
                    dglen=0
    return s
    