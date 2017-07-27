# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:24:46 2016

@author: Nathan
"""

import time

start_time = time.time()


f= open("p082_matrix.txt", "r")
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
starts = map(lambda x: (x,0), range(dimension))
unvisitednodes = []
visitednodes = []
nodes = {}
origin = node("Origin", 0, starts)
end = node("End", float("inf"), None)
visitednodes.append("Origin")
nodes["Origin"] = origin

def is_real(coor):
    if coor[0] >=0 and coor[0] < dimension and coor[1] >= 0 and coor[1] < dimension:
        return True
    else:
        return False


for x in range(dimension):
    for y in range(dimension):
        neighbors = []
        if is_real((x-1,y)):
            neighbors.append((x-1,y))
        if is_real((x,y+1)):
            neighbors.append((x,y+1))
        if not is_real((x,y+1)):
            neighbors.append("End")
        if is_real((x+1,y)):
            neighbors.append((x+1,y))
            
        newNode = node((x,y), float("inf"), neighbors)
        unvisitednodes.append((x,y))
        nodes[(x,y)] = newNode


unvisitednodes.append("End")
nodes["End"] = end

def visit_next():
    smallestDistance = float("inf")
    
    for node in unvisitednodes:
        if nodes[node].distanceFromOrigin < smallestDistance:
            smallestDistance = nodes[node].distanceFromOrigin
            nextNode = node
    return nextNode

def output_file(counter, currentNode):
    f = open("output" + counter +".csv", "w") 
    for x in range(dimension):
        line = ""
        for y in range(dimension):
            if (x,y) == currentNode:
                line = line + ",***" + str(nodes[currentNode].distanceFromOrigin) + "***"
            if (visitednodes.count((x,y)) == 1) and (x,y) != currentNode:
                line = line + ",_" + str(nodes[(x,y)].distanceFromOrigin) +"_"
            if (visitednodes.count((x,y)) != 1) and (x,y) != currentNode:
                line = line + "," + str(nodes[(x,y)].distanceFromOrigin) 
        line = line + "\n"
        f.write(line)
    f.close()



for node in visitednodes:

    for neighborID in nodes[node].listOfNeighbors:
        neighbor = nodes[neighborID]
        if neighborID =="End":
            tentativeDistance = nodes[node].distanceFromOrigin
        else:
            tentativeDistance = nodes[node].distanceFromOrigin + Matrix[neighborID[0]][neighborID[1]]
        if (tentativeDistance < neighbor.distanceFromOrigin):
            neighbor.distanceFromOrigin = tentativeDistance
    nextVisit = visit_next()
    visitednodes.append(unvisitednodes.pop(unvisitednodes.index(nextVisit)))

    if visitednodes.count("End") == 1:
        print nodes["End"].distanceFromOrigin
        break





#for s in starts:
#    node = nodes[s]
#    node.distanceFromOrigin = Matrix[node.ID[0]][node.ID[1]]
#    
#for s in starts:
#    node = nodes[s]   
#    if nodes[s].listOfNeighbors != []:  
#        for neighborID in node.listOfNeighbors: #neighbor is the 2-tuple representing the coordinates of the adjacent node  
#            neighbor = nodes[neighborID]
#            if neighbor.distanceFromOrigin > (node.distanceFromOrigin + Matrix[neighbor.ID[0]][ neighbor.ID[1]]):
#                neighbor.distanceFromOrigin = (node.distanceFromOrigin + Matrix[neighbor.ID[0]][ neighbor.ID[1]])
#
#print nodes[(4,4)].distanceFromOrigin
#
#print len(nodes)
print("--- %s seconds ---" % (time.time() - start_time))