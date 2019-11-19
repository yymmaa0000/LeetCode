# 358. Rearrange String k Distance Apart
# Hard
# 29514FavoriteShare
# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
# Example 1:
# Input: s = "aabbcc", k = 3
# Output: "abcabc" 
# Explanation: The same letters are at least distance 3 from each other.
# Example 2:
# Input: s = "aaabc", k = 3
# Output: "" 
# Explanation: It is not possible to rearrange the string.
# Example 3:
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k ==0: return s
        dic = {}
        for x in s:
            if x in dic: dic[x] += 1
            else: dic[x] = 1
        result = ""
        heap = []
        for x in dic.keys():
            heap.append([-dic[x],x])
        heapq.heapify(heap)
        queue = []
        for i in range(len(s)):
            if len(heap) == 0: return ""
            current = heapq.heappop(heap)
            result += current[1]
            current[0] += 1
            queue.append(current)
            if len(queue) == k:
                add = queue.pop(0)
                if add[0] < 0: heapq.heappush(heap,add)
        return result
