# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:55:56 2016

@author: Nathan
"""

import time
import numpy
start_time = time.time()



#probability to roll a number between 2 and 8
maxroll = 8
rollProb = {}
rollProb[2] = 1.0/16
rollProb[3] = 2.0/16
rollProb[4] = 3.0/16
rollProb[5] = 4.0/16
rollProb[6] = 3.0/16
rollProb[7] = 2.0/16
rollProb[8] = 1.0/16

yesDoubleProb = dict(zip(range(2,maxroll+1), [1, 0, 1.0/3, 0, 1.0/3, 0, 1]))
noDoubleProb = dict(zip(range(2,maxroll+1), [0, 1, 2.0/3, 1, 2.0/3, 1, 0]))

doubleProb = dict(zip([0,1,2,3], [noDoubleProb, yesDoubleProb, yesDoubleProb, yesDoubleProb]))

nextDoubl = {}
nextDoubl[0] = [0,1]
nextDoubl[1] = [0,2]
nextDoubl[2] = [0,3]
#making chance outcome probabilities
chance7spaces = [0,4,5,7,10,11,12,15,24,39]
chance22spaces = [0,10,11,24,39,5,25,28,19,22]
chance36spaces = [0,10,11,24,39,5,12,36,33]

chance7probs =  [1.0/16,1.0/16,1.0/16,6.0/16,1.0/16,1.0/16,1.0/16,2.0/16,1.0/16,1.0/16]
chance22probs = [1.0/16,1.0/16,1.0/16,1.0/16,1.0/16,1.0/16,2.0/16,1.0/16,1.0/16,6.0/16]
chance36probs = [(1.0/16)+(1.0/16)*(1.0/16),(1.0/16)+(1.0/16)*(1.0/16),1.0/16,1.0/16,1.0/16,3.0/16,1.0/16,6.0/16,(1.0/16)*(14.0/16)]

chance7 = dict(zip(chance7spaces, chance7probs))
chance22 = dict(zip(chance22spaces, chance22probs))
chance36 = dict(zip(chance36spaces, chance36probs))

chance = dict(zip([7,22,36], [chance7, chance22, chance36]))

#making community chest probabilities
cc2spaces = [0,10,2]
cc17spaces = [0,10,17]
cc33spaces = [0,10,33]

cc2probs = [1.0/16,1.0/16,14.0/16]
cc17probs = [1.0/16,1.0/16,14.0/16]
cc33probs = [1.0/16,1.0/16,14.0/16]

cc2 = dict(zip(cc2spaces, cc2probs))
cc17 = dict(zip(cc17spaces, cc17probs))
cc33 = dict(zip(cc33spaces, cc33probs))

cc = dict(zip([2,17,33], [cc2,cc17,cc33]))

#making sample space
counter = 0

sampleSpace = {}
sampleSpaceReverse = {}
for space in range(40):
    for dub in range(3):
        sampleSpace[counter] = (space, dub)
        sampleSpaceReverse[(space,dub)] = counter
        counter +=1 
    sampleSpaceReverse[(space, 3)] = 30



#making markov chain matrix using my method
markovList = []
for i in range(120):
    markovList.append([])
    for j in range(120):
        markovList[i].append(0)

for i in range(120):
    dub = sampleSpace[i][1]
    currSpace = sampleSpace[i][0]
    for roll in range(2,maxroll+1):
        nextSpace = (currSpace+roll)%40
        for dubScenario in nextDoubl[dub]:# account for getting either doubles next or not
            if nextSpace == 7 or nextSpace == 22 or nextSpace == 36: #chance
                for space, prob in chance[nextSpace].iteritems():
                    markovList[i][sampleSpaceReverse[(space,dubScenario)]] += (rollProb[roll]*prob*doubleProb[dubScenario][roll])
                continue
            if nextSpace == 2 or nextSpace == 17 or nextSpace == 33: #communitychest
                for space, prob in cc[nextSpace].iteritems():
                    markovList[i][sampleSpaceReverse[(space,dubScenario)]] += (rollProb[roll]*prob*doubleProb[dubScenario][roll])
                continue
            if nextSpace == 30 and dubScenario == 0:#go to jail
                markovList[i][30] += rollProb[roll]
                continue
            if nextSpace == 30 and dubScenario != 0:#careful of double counting, we go to jail no matter if doubles or not
                continue
            markovList[i][sampleSpaceReverse[(nextSpace,dubScenario)]] += (rollProb[roll]*doubleProb[dubScenario][roll])


    
markovMatrix = numpy.matrix(markovList)

#transform probDist with markov matrix until probabilities converge
probDist = numpy.matrix([1]+[0]*119)

for i in range(10000):
    probDist = probDist*markovMatrix
    
output = probDist.tolist()[0]
probs = []
for i in range(0,120,3):
    probs.append(sum(output[i:i+3]))
    
print probs[10], probs[24], probs[0]




#for 6 sided die, 2 - 12
#rollProb = {}
#rollProb[2] = 1.0/36
#rollProb[3] = 2.0/36
#rollProb[4] = 3.0/36
#rollProb[5] = 4.0/36
#rollProb[6] = 5.0/36
#rollProb[7] = 6.0/36
#rollProb[8] = 5.0/36
#rollProb[9] = 4.0/36
#rollProb[10] = 3.0/36
#rollProb[11] = 2.0/36
#rollProb[12] = 1.0/36
#
#yesDoubleProb = dict(zip(range(2,13), [1, 0, 1.0/3, 0, 1.0/5, 0, 1.0/5, 0, 1.0/3, 0, 1]))
#noDoubleProb = dict(zip(range(2,13), [0, 1, 2.0/3, 1, 4.0/5, 1, 4.0/5, 1, 2.0/3, 1, 0]))



print("--- %s seconds ---" % (time.time() - start_time))