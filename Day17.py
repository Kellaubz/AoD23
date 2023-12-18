#!/usr/bin/python3
# -*- coding: utf-8 -*-

import heapq

## Part 1

# First try, 13h to compute the value

# def init_graph(lines):
#     graph={}
#     n=len(lines)
#     m=len(lines[0])-1
#     for i in range(n):
#         for j in range(m):
#             for k in range(1,4):
#                 for d in ['n','s','e','w']:
#                     node=(i,j,k,d)
#                     if node_is(node,n,m):
#                         Nb=neighbour(node,n,m)
#                         v=[]
#                         for nb in Nb:
#                             v.append((nb,int(lines[nb[0]][nb[1]])))
#                         graph[node]=v
#     return graph

# def node_is(node,n,m):
#     i,j,k,d=node
#     if i<0 or i>=n or j<0 or j>=m:
#         return False
#     if d=='n':
#         if i<k:
#             return False
#     if d=='s':
#         if i>=n-k:
#             return False
#     if d=='w':
#         if j<k:
#             return False
#     if d=='e':
#         if j>=m-k:
#             return False
#     return True
    
# def neighbour(node,n,m):
#     i,j,k,d=node
#     res=[]
#     if d!='n' and d!='s':
#         res.append((i+1,j,1,'n'))
#         res.append((i-1,j,1,'s'))
#     elif k!=3:
#         res.append((i+1,j,k+1,d))
#     if d!='w' and d!='e':
#         res.append((i,j+1,1,'w'))
#         res.append((i,j-1,1,'e'))
#     elif k!=3:
#         res.append((i,j+1,k+1,d))
#     rres=[]
#     for r in res:
#         if node_is(r,n,m):
#             rres.append(r)
#     return rres

# def dijkstra(graph, sources,n,m):
#     unvisited=set(graph.keys())
#     distances={}
#     prev={}
#     for node in unvisited:
#         distances[node]=float('inf')
#     for node in sources:
#         distances[node]=sources[node]
#     stop=4
#     while unvisited:
#         min_node=None
#         for node in unvisited:
#             if min_node is None:
#                 min_node=node
#             elif distances[node]<distances[min_node]:
#                 min_node=node
#         unvisited.remove(min_node)
#         if (min_node[0],min_node[1])==(n-1,m-1):
#             stop-=1
#             if stop==0:
#                 min_dist=float('inf')
#                 for node in distances:
#                     if (node[0],node[1])==(n-1,m-1):
#                         if distances[node]<min_dist:
#                             min_dist=distances[node]
#                 return min_dist
#         for node, weight in graph[min_node]:
#             if node in unvisited:
#                 new_distance=distances[min_node]+weight
#                 if new_distance<distances[node]:
#                     distances[node]=new_distance
#                     prev[node]=min_node
#     return distances,prev

# def find_shortest_3more(file):
#     f=open(file,'r')
#     lines=f.readlines()
#     f.close()
#     n=len(lines)
#     m=len(lines[0])-1
#     graph=init_graph(lines)
#     sources={(1,0,1,'n'):int(lines[0][1]),(0,1,1,'w'):int(lines[0][1])}
#     #distances,prev=dijkstra(graph,sources)
#     return dijkstra(graph,sources,n,m)
#     min_dist=float('inf')
#     for node in distances:
#         if (node[0],node[1])==(n-1,m-1):
#             if distances[node]<min_dist:
#                 min_dist=distances[node]
#     return min_dist

## Second try, use heapq seems faster

def find_shortest_less3(file):
    f=open(file,'r')
    lines=f.readlines()
    f.close()
    lines=[list(int(y) for y in list(x.strip())) for x in lines]
    n=len(lines)
    m=len(lines[0])
    visited=set()
    priority_queue=[(0,0,0,5,5,0)] # init at 5,5
    while priority_queue:
        weight,i,j,diri,dirj,step = heapq.heappop(priority_queue)
        if (i,j)==(n-1,m-1):
            return weight
        if not((i,j,diri,dirj,step) in visited):
            visited.add((i,j,diri,dirj,step))
            if step<3 and (diri,dirj)!=(5,5): # same direction
                x,y=i+diri,j+dirj
                if 0<=x<n and 0<=y<m:
                    heapq.heappush(priority_queue,(weight+lines[x][y],x,y,diri,dirj,step+1))
            for new_diri,new_dirj in [(1,0),(-1,0),(0,1),(0,-1)]: # new direction
                if (new_diri,new_dirj)!=(diri,dirj) and (new_diri,new_dirj)!=(-diri,-dirj):
                    x,y=i+new_diri,j+new_dirj
                    if 0<=x<n and 0<=y<m:
                        heapq.heappush(priority_queue,(weight+lines[x][y],x,y,new_diri,new_dirj,1))

## Part 2
                        
def find_shortest_less10more4(file):
    f=open(file,'r')
    lines=f.readlines()
    f.close()
    lines=[list(int(y) for y in list(x.strip())) for x in lines]
    n=len(lines)
    m=len(lines[0])
    visited=set()
    priority_queue=[(0,0,0,5,5,0)] # init at 5,5
    while priority_queue:
        weight,i,j,diri,dirj,step = heapq.heappop(priority_queue)
        if step>=4 and (i,j)==(n-1,m-1):
            return weight
        if not((i,j,diri,dirj,step) in visited):
            visited.add((i,j,diri,dirj,step))
            if step<10 and (diri,dirj)!=(5,5): # same direction
                x,y=i+diri,j+dirj
                if 0<=x<n and 0<=y<m:
                    heapq.heappush(priority_queue,(weight+lines[x][y],x,y,diri,dirj,step+1))
            if step>=4 or (diri,dirj)==(5,5): # new direction
                for new_diri,new_dirj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (new_diri,new_dirj)!=(diri,dirj) and (new_diri,new_dirj)!=(-diri,-dirj):
                        x,y=i+new_diri,j+new_dirj
                        if 0<=x<n and 0<=y<m:
                            heapq.heappush(priority_queue,(weight+lines[x][y],x,y,new_diri,new_dirj,1))                        