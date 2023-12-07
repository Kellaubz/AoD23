#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

def card_to_int(card):
    if card.isdigit():
        return int(card)
    elif card=='T':
        return 10
    elif card=='J':
        return 11
    elif card=='Q':
        return 12
    elif card=='K':
        return 13
    elif card=='A':
        return 14
    raise ValueError
    
def value(cnt):
    if cnt==[1,1,1,1,1]:
        return 0
    elif cnt==[2,1,1,1]:
        return 1
    elif cnt==[2,2,1]:
        return 2
    elif cnt==[3,1,1]:
        return 3
    elif cnt==[3,2]:
        return 4
    elif cnt==[4,1]:
        return 5
    elif cnt==[5]:
        return 6
    raise ValueError

def value_hand(hand):
    S=set(hand)
    cnt=[]
    for i in S:
        cnt.append(hand.count(i))
    cnt.sort(reverse=True)
    return value(cnt)

def camel_rank(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    hands=[]
    for i in range(len(lines)):
        bid=int(lines[i][5:-1])
        h=[card_to_int(lines[i][j]) for j in range(5)]
        val=value_hand(h)
        hands.append([val,h,bid])
    hands.sort()
    m=0
    for i in range(len(hands)):
        m=m+hands[i][2]*(i+1)
    return m
    
## Part 2

def card_to_int_joker(card):
    if card=='J':
        return 0
    else:
        return card_to_int(card)

def value_hand_joker(hand):
    S=set(hand)
    j=hand.count(0)
    cnt=[]
    for i in S:
        if i!=0:
            cnt.append(hand.count(i))
    if cnt==[]:
        cnt=[0]
    cnt.sort(reverse=True)
    cnt[0]=cnt[0]+j    
    return value(cnt)

def camel_joker(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    hands=[]
    for i in range(len(lines)):
        bid=int(lines[i][5:-1])
        h=[card_to_int_joker(lines[i][j]) for j in range(5)]
        val=value_hand_joker(h)
        hands.append([val,h,bid])
    hands.sort()
    m=0
    for i in range(len(hands)):
        m=m+hands[i][2]*(i+1)
    return m