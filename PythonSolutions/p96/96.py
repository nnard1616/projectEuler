# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:24:46 2016

@author: Nathan
"""

import time

start_time = time.time()
f= open("p096_sudoku.txt", "r")
rows = []
for line in f.readlines():
    if line.find("Grid") == -1:
        rows.append(list(line)[0:9])
    if len(rows) == 9:
        break
f.close()

cubeDict = dict()

for i in range(9):
    for j in range(9):
        if i <3 and j<3:
            cubeDict[(i,j)] = 0
        if i >=3 and i < 6 and j >= 0 and j < 3:
            cubeDict[(i,j)] = 1
        if i >=6 and i < 9 and j >= 0 and j < 3:
            cubeDict[(i,j)] = 2
        if i >=0 and i < 3 and j >= 3 and j < 6:
            cubeDict[(i,j)] = 3
        if i >=3 and i < 6 and j >= 3 and j < 6:
            cubeDict[(i,j)] = 4
        if i >=6 and i < 9 and j >= 3 and j < 6:
            cubeDict[(i,j)] = 5
        if i >=0 and i < 3 and j >= 6 and j < 9:
            cubeDict[(i,j)] = 6
        if i >=3 and i < 6 and j >= 6 and j < 9:
            cubeDict[(i,j)] = 7
        if i >=6 and i < 9 and j >= 6 and j < 9:
            cubeDict[(i,j)] = 8
    
columns = [[],[],[],[],[],[],[],[],[]]
for row in rows:
    i = 0
    for c in row:
        columns[i].append(c)
        i+=1
cubes = [[],[],[],[],[],[],[],[],[]]
cube = -3
for row in rows:
    if rows.index(row)%3 ==0:
        cube+=3
    cubes[cube].extend(row[:3])
    cubes[cube+1].extend(row[3:6])  
    cubes[cube+2].extend(row[6:])
    
cells = [[],[],[],[],[],[],[],[],[]]
for cell in cells:
    cell.extend([[],[],[],[],[],[],[],[],[]])



print cubes
print("--- %s seconds ---" % (time.time() - start_time))