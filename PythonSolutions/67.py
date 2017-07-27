# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:24:46 2016

@author: Nathan
"""

import time

start_time = time.time()

#exampleTriangle = [[3],[7,4],[2,4,6],[8,5,9,3]]
f= open("p067_triangle.txt", "r")
lines = f.readlines()
f.close()

exampleTriangle = []
for line in lines:
    line = map(int, line.split())
    exampleTriangle.append(line)
    
class node: 
    def __init__(self, ID, distanceFromOrigin, listOfNeighbors):
        self.distanceFromOrigin = distanceFromOrigin
        self.listOfNeighbors = listOfNeighbors
        self.ID = ID

origin = node("Origin", 0, [(0,0)])
nodes = [[origin]]

for row in exampleTriangle:
    x = exampleTriangle.index(row)
    nodeSet = []
    y=-1
    for cell in row:
        y +=1
        try:
            exampleTriangle[x+1]
            newNode = node((x,y), float("-inf"), [(x+1,y),  (x+1, y+1)])
        except:
            newNode = node((x,y), float("-inf"), None)
        nodeSet.append(newNode)
    nodes.append(nodeSet)

for nodeSet in nodes:
    for NODE in nodeSet:
        if NODE.listOfNeighbors != None:  
            for neighborID in NODE.listOfNeighbors: #neighbor is the 2-tuple representing the coordinates of the adjacent node 
                
                neighbor = nodes[neighborID[0]+1][neighborID[1]]
#                print NODE.ID, neighborID, neighbor.ID
                if neighbor.distanceFromOrigin < (NODE.distanceFromOrigin + exampleTriangle[neighbor.ID[0]][ neighbor.ID[1]]):
                    neighbor.distanceFromOrigin = (NODE.distanceFromOrigin + exampleTriangle[neighbor.ID[0]][ neighbor.ID[1]])

maxSum = 0
for n in nodes[-1]:
    maxSum = max(maxSum, n.distanceFromOrigin)
print maxSum
print("--- %s seconds ---" % (time.time() - start_time))