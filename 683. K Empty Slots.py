# 683. K Empty Slots
# Hard
# 490518FavoriteShare
# You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.
# You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.
# Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.
# If there isn't such day, return -1.
 
# Example 1:
# Input: 
# bulbs: [1,3,2]
# K: 1
# Output: 2
# Explanation:
# On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
# On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
# On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
# We return 2 because on the second day, there were two on bulbs with one off bulb between them.
# Example 2:
# Input: 
# bulbs: [1,2,3]
# K: 1
# Output: -1
 
# Note:
# 1.  1 <= N <= 20000
# 2.  1 <= bulbs[i] <= N
# 3.  bulbs is a permutation of numbers from 1 to N.
# 4.  0 <= K <= 20000
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        my_Ass = [0]*len(bulbs)
        for key,val in enumerate(bulbs):
            my_Ass[val-1] = key+1 
        bulbs = my_Ass
        #print(bulbs)
        l = 0 
        r = K+1
        result = 2**31
        while r < len(bulbs):
            great = True
            for i in range(l+1,r):
                if bulbs[i] < bulbs[l] or bulbs[i] < bulbs[r]:
                    l = i
                    r = l + K + 1
                    great = False
                    break
            if great:
                result = min(result,max(bulbs[l],bulbs[r]))
                l += 1
                r += 1
            #print(l,r,result)
        if result == 2**31: result = -1
        return result
