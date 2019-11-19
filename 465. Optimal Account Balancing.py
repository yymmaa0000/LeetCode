# 465. Optimal Account Balancing
# Hard
# 27848FavoriteShare
# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
# Note:
# 1.  A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# 2.  Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
# Example 1:
# Input:
# [[0,1,10], [2,0,5]]

# Output:
# 2

# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.

# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
# Example 2:
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

# Output:
# 1

# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.

# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
# from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        people = defaultdict(int)
        for x,y,z in transactions:
            people[x] -= z
            people[y] += z
        #print(people)
        debt = []
        for x in people.values():
            if x != 0: debt.append(x)
        #print(debt)
        
        def dfs(start):
            #print(start,"=>")
            while start < len(debt) and debt[start] == 0: start += 1
            result = 2**31
            seen = set()
            for i in range(start+1,len(debt)):
                if debt[i] not in seen and debt[i]*debt[start] < 0:
                    if start == 0: print(debt)
                    debt[i] += debt[start]
                    result = min(result,dfs(start+1)+1)
                    #print(i,result,"aaaaaa")
                    debt[i] -= debt[start]
                    seen.add(debt[i])
            if result == 2**31: result = 0
            #print(start,result)
            return result
        return dfs(0)
