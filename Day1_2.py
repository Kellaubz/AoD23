#!/usr/bin/python3
# -*- coding: utf-8 -*-

number=['one','two','three','four','five','six','seven','eight','nine']

def letter_number(pos,string):
    for i in range(len(number)):
        if string[pos:pos+len(number[i])]==number[i]:
            return i+1
    return 0
    

def trebuchet_2(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for line in lines:
        l=0
        f=0
        for i in range(len(line)):
            try :
                l=int(line[i])
            except:
                tmp=letter_number(i,line)
                if tmp!=0:
                    l=tmp
            if f==0:
                f=l
        s=s+10*f+l
    return s
    