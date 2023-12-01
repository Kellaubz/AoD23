#!/usr/bin/python3
# -*- coding: utf-8 -*-

def trebuchet(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    s=0
    for line in lines:
        l=0
        f=0
        for char in line:
            try :
                l=int(char)
                if f==0:
                    f=l
            except:
                pass
        s=s+10*f+l
    return s
            
        
