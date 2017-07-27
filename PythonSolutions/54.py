# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:47:41 2016

@author: Nathan
"""
f = open("poker.txt", "r")
lines = f.readlines()
f.close()

import time
start_time = time.time()

d = dict(zip(["2","3","4","5","6","7","8","9","T","J","Q","K","A"],range(1,14)))

        
def quickSortCards(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splipairsoint = partition(alist,first,last)

       quickSortHelper(alist,first,splipairsoint-1)
       quickSortHelper(alist,splipairsoint+1,last)


def partition(alist,first,last):
   pivotvalue = d[alist[first][0]]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and d[alist[leftmark][0]] <= pivotvalue:
           leftmark = leftmark + 1

       while d[alist[rightmark][0]] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
   


def hand(inString):
    
    cards = inString.split()
    quickSortCards(cards)
    Hcount = inString.count("H")
    Dcount = inString.count("D")
    Ccount = inString.count("C")
    Scount = inString.count("S")
#    print cards
    SF = 0 # 0 or 1
    FK = 0 # 0 or 1
    FH = 0 # 1,..,13
    F = 0 # 0 or 1
    S = 0 # 0 or 1
    TK = 0 # 1,...,13
    TP = 0 # 0 or 1
    pairs = [] #
    HC = []
    for card in cards:
        HC.append(d[card[0]])
    HC.reverse()
    
    lSet = max(Hcount,Dcount,Ccount,Scount)

    if  lSet ==5: F = 1 #Flush
    for card in cards[:-1]: #Check if Straight
        
        if d[card[0]] != d[cards[cards.index(card)+1][0]]-1:
            S = 0
            break
        else:
            S = 1
    
    for card in cards:
        valCount = inString.count(card[0])
        if  valCount == 4:
            FK =1
            break
        if valCount ==3:
            TK = d[card[0]]
            
        if valCount ==2:
            inString = inString.replace(card[0], "")
            pairs.append(d[card[0]])
    pairs.sort()
    pairs.reverse()
    if len(pairs) == 2: TP = 1
    while len(pairs) < 2:
        pairs.append(0)
    
    
    if TK and pairs.count(0) == 1:
        FH = 1
        FH = TK
    
#    if cards[0][0] == "2" and cards[1][0] =="3" and cards[2][0] =="4" and cards[3][0] == "5" and cards[4][0] == "A":
#        S = 1
#        HC = 4
    

    if F and S: SF = 1
    score = [SF, #SF
                  FK, #FK
                  FH, #FH
                  F, #F
                  S, #S
                  TK, #TK
                  TP,
                  pairs, #pairs
                  HC]
    return score
   
        
#inS = "8C 8D 8H TC JC 9D 9H 9C 2D 2D\n"
#
#sort = inS.split()
#quickSortCards(sort)
#
#print sort
#
#player1 = hand(inS[0:14])
#player2 = hand(inS[15:])
#
#
#print player1
#print player2
#if player1 > player2:
#    print "win"
#else:
#    print "lose"

wins = 0
#lines = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD", "5D 8C 9S JS AC 2C 5C 7D 8S QH","2D 9C AS AH AC 3D 6D 7D TD QD", "4D 6S 9H QH QC 3D 6D 7H QD QS","2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"] 
for line in lines:
    player1 = hand(line[0:14])
    player2 = hand(line[15:])
    if player1 > player2:
#        if player1[6].count(0) == 0:
#            print player1, "\n", player2,  "win\n"
        wins+=1
#    else:
#        if player1[6].count(0) == 0:
#            print player1, "\n", player2, "lose\n"

print wins
print("--- %s seconds ---" % (time.time() - start_time))