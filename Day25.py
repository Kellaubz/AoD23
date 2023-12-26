#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Part 1

import networkx as nx

def cut_graph(G):
    cut_value, partition = nx.stoer_wagner(G)
    return len(partition[0])*len(partition[1])

def cut_wire(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    G = nx.Graph()
    for line in lines:
        [key,line] = line[:-1].split(':')
        sons = line.split(' ')[1:]
        for son in sons:
            G.add_edge(key,son)
    return cut_graph(G)