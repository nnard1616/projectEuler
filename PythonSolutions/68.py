# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:15:41 2016

@author: Nathan
"""

import time
from itertools import permutations as perm
start_time = time.time()

def subset_sum(numbers, target, maxNums, sets = [], partial=[]):
    s = sum(partial)
    
    if s == target and len(partial) == maxNums:
        try: 
            ind = partial.index(10)
            ten = [partial.pop(ind)]
            for i in list(perm(partial)):
                sets.append(ten+list(i))
        except:
            for i in list(perm(partial)):
                sets.append(list(i))
    if s == target and len(partial) != maxNums:
        return
    if s > target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        
        remaining = numbers[i+1:]
        
        subset_sum(remaining, target, maxNums, sets, partial + [n] )
    return sets
    
    
def find_solution(sets, remaining, solution=[]):#
    
    if len(solution) ==5:
        return 
    if len(solution) ==4:
        remaining.append(solution[0][1])
    for s in sets:
        current = solution[-1]
        if s[1] == current[2] and len(list(set(s).intersection(set(remaining))))==3:
            if len(solution) == 4:
                if solution[0][1] == s[2]:
                    solution.append(s)
                    return solution
            if len(solution) <4:
                remaining = list(set(remaining).difference(set(s[:2])))
                solution.append(s)
                current = s
                find_solution(sets, remaining, solution)
    if len(solution) == 4:
        remaining.remove(solution[0][1])
    if len(solution) != 5:
        remaining += solution[-1][:2]
        solution.pop(-1)
    if len(solution) == 5:
        return solution
        
        
def p68():
    junks = []
    for n in range(13,21):
        junks.append(subset_sum(range(1,11), n, 3, []))
    
    maxSol = 0
    for junk in junks:
        for j in junk:
            if j[0] == 10:
                sol = find_solution(junk, list(set(range(1,11)).difference(set(j[:2]))), [j])
                if sol != None:            
                    sol.sort()
                    sol = int(''.join(map(str, sum(sol, []))))
                    maxSol = max(maxSol, sol)
    return maxSol

print p68()
print("--- %s seconds ---" % (time.time() - start_time))