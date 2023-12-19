#!/usr/bin/python3
# -*- coding: utf-8 -*-

from copy import deepcopy

cat_to_int={'x':0,'m':1,'a':2,'s':3}

## Part 1

def init_dico(rule_block):
    res={}
    for line in rule_block:
        val=[]
        [key,rules]=line.split('{')
        rules=rules[:-1].split(',')
        for rule in rules:
            tmp=rule.split(':')
            v=[]
            if len(tmp)==2:
                v=[cat_to_int[tmp[0][0]],tmp[0][1],int(tmp[0][2:]),tmp[1]]
            else:
                v=[None,None,None,tmp[0]]
            val.append(v)
        res[key]=val
    return res

def init_part(part_block):
    res=[]
    for line in part_block:
        part=[int(l[2:]) for l in line[1:-1].split(',')]
        res.append(part)
    return res

def check_rule(rule,part):
    if rule[0]==None:
        return True
    else:
        if rule[1]=='>':
            return part[rule[0]]>rule[2]
        elif rule[1]=='<':
            return part[rule[0]]<rule[2]
        else:
            raise ValueError('Unknown operator')

def accepted_part(file):
    f=open(file,'r')
    [rule_block,part_block]=f.read().split('\n\n')
    f.close()
    rules_dic=init_dico(rule_block.split('\n'))
    parts=init_part(part_block.split('\n')[:-1])
    res=0
    for part in parts:
        key='in'
        process=True
        while process:
            rules=rules_dic[key]
            for rule in rules:
                if check_rule(rule,part):
                    key=rule[3]
                    break
            if key=='A':
                res+=sum(part)
                process=False
            elif key=='R':
                process=False
    return res

## Part 2

def cut_interval(rule,part):
    if rule[0]==None:
        return (None,part)
    else:
        if rule[1]=='>':
            if part[rule[0]][0]>=rule[2]:
                return (None,part)
            elif part[rule[0]][1]<=rule[2]:
                return (part,None)
            else:
                p1=deepcopy(part)
                p2=deepcopy(part)
                p1[rule[0]][1]=rule[2]
                p2[rule[0]][0]=rule[2]
                return (p1,p2)
        elif rule[1]=='<':
            if part[rule[0]][1]<rule[2]:
                return (None,part)
            elif part[rule[0]][0]>=rule[2]-1:
                return (part,None)
            else:
                p1=deepcopy(part)
                p2=deepcopy(part)
                p1[rule[0]][1]=rule[2]-1
                p2[rule[0]][0]=rule[2]-1
                return (p2,p1)
        else:
            raise ValueError('Unknown operator')

def nb_part_accepted(file):
    f=open(file,'r')
    [rule_block,_]=f.read().split('\n\n')
    f.close()
    rules_dic=init_dico(rule_block.split('\n'))
    part_interval=[[[0,4000],[0,4000],[0,4000],[0,4000],'in',0]]
    s=0
    while part_interval:
        part=part_interval.pop(0)
        rules=rules_dic[part[4]]
        i=part[5]
        rule=rules[i]
        (ref,acc)=cut_interval(rule,part)
        to_add=[]
        if acc!=None:
            if rule[3]=='A':
                s+=(acc[0][1]-acc[0][0])*(acc[1][1]-acc[1][0])*(acc[2][1]-acc[2][0])*(acc[3][1]-acc[3][0])
            elif rule[3]=='R':
                pass
            else:
                acc[4]=rule[3]
                acc[5]=0
                to_add.append(acc)
        if ref!=None:
            ref[5]=i+1
            to_add.append(ref)
        part_interval=to_add+part_interval
    return s


