# 1136. Parallel Courses
# Hard
# 304FavoriteShare
# There are N courses, labelled from 1 to N.
# We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.
# In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.
# Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.
 
# Example 1:
 
# Input: N = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: 
# In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
# Example 2:
 
# Input: N = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: 
# No course can be studied because they depend on each other.
 
# Note:
# 1.  1 <= N <= 5000
# 2.  1 <= relations.length <= 5000
# 3.  relations[i][0] != relations[i][1]
# 4.  There are no repeated relations in the input.


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        child = collections.defaultdict(list)
        parents = [0]*N
        for x,y in relations:
            child[x].append(y)
            parents[y-1] += 1

        result = 0
        can_take = []
        for key,val in enumerate(parents):
            if val == 0: can_take.append(key+1)

        taken = 0
        while can_take:
            result += 1
            temp = []
            taken += len(can_take)
            for x in can_take:
                for y in child[x]:
                    parents[y-1] -= 1
                    if parents[y-1] == 0: temp.append(y)
            can_take = temp

        if taken != N: return -1
        else: return result
