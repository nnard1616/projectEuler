# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:24:46 2016

@author: Nathan
"""

import time

start_time = time.time()


f= open("p81Ex.txt", "r")
lines = f.readlines()
f.close()

Matrix = []
for line in lines:
    line = map(int, line.split(','))
    Matrix.append(line)
dimension = len(Matrix)   
class node: 
    def __init__(self, ID, distanceFromOrigin, listOfNeighbors):
        self.distanceFromOrigin = distanceFromOrigin
        self.listOfNeighbors = listOfNeighbors
        self.ID = ID

origin = node("Origin", 0, [(0,0)])
nodes = [[origin]]

def is_real(coor):
    try:
        Matrix[coor[0]][coor[1]]
        return True
    except:
        return False
        
for i in range(dimension*2-1):
    nodeSet = []
    if i >= dimension:
        x0 = dimension-1
    else:
        x0 = i
    for x in range(x0, i-(x0+1), -1):
        y = i-x
        if (x < dimension-1) and (y < dimension-1):
            newNode = node((x,y), float("inf"), [(x+1,y),  (x, y+1)])
        if (x < dimension-1) and not (y < dimension-1):
            newNode = node((x,y), float("inf"), [(x+1,y)])
        if not (x < dimension-1) and (y < dimension-1):
            newNode = node((x,y), float("inf"), [(x, y+1)])
        if not (x < dimension-1) and not (y < dimension-1):
            newNode = node((x,y), float("inf"), None)
        nodeSet.append(newNode)
    nodes.append(nodeSet)

for nodeSet in nodes:
    for NODE in nodeSet:
        if NODE.listOfNeighbors != None:  
            for neighborID in NODE.listOfNeighbors: #neighbor is the 2-tuple representing the coordinates of the adjacent node  
                i = sum(neighborID)
                if i >= dimension:
                    neighbor = nodes[i+1][neighborID[1]-(i-(dimension-1))]
                else:
                    neighbor = nodes[i+1][neighborID[1]]
                
                if neighbor.distanceFromOrigin > (NODE.distanceFromOrigin + Matrix[neighbor.ID[0]][ neighbor.ID[1]]):
                    neighbor.distanceFromOrigin = (NODE.distanceFromOrigin + Matrix[neighbor.ID[0]][ neighbor.ID[1]])

print nodes[-1][0].distanceFromOrigin

print len(nodes)
print("--- %s seconds ---" % (time.time() - start_time))