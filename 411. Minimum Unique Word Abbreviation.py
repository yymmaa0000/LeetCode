# 411. Minimum Unique Word Abbreviation
# Hard
# 100103FavoriteShare
# A string such as "word" contains the following abbreviations:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.
# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.
# Note:
# •   In the case of multiple answers as shown in the second example below, you may return any one of them.
# •   Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # reference https://leetcode.com/problems/minimum-unique-word-abbreviation/discuss/89880/C%2B%2B-Bit-Manipulation-%2B-DFS-solution
        n = len(target)
        limit = 1<<n
        bit_list = []
        all_diff_bits = 0
        for x in dictionary:
            if len(x) != n: continue
            temp = 0
            bit = 1
            for i in reversed(range(n)):
                if x[i] != target[i]: temp += bit
                bit <<= 1
            bit_list.append(temp)
            all_diff_bits = all_diff_bits | temp
        #print(bit_list,all_diff_bits)
        
        def get_word_length(mask):
            # Return the length of abbreviation given bit sequence
            cnt = 0
            bit = 1
            i = 0
            while i < n:
                if mask & bit:
                    cnt += 1
                    bit <<= 1
                    i+=1
                else:
                    while i < n and mask & bit == 0:
                        bit <<= 1
                        i+=1
                    cnt += 1
                
            return cnt
        #print(get_word_length(16))
        
        def dfs(bit,mask,best): 
            length = get_word_length(mask)
            if length >= best[0]: return
            is_valid = True
            for x in bit_list:
                if mask & x == 0:
                    is_valid = False
                    break
            if is_valid:
                best[0] = length
                best[1] = mask
            else:
                for i in range(bit+1,n+1):
                    next_bit = 1<<(i-1)
                    if next_bit & all_diff_bits: dfs(i,mask+next_bit,best)
        best = [n+1,2**n] # [length of abbreviation, actual mask]
        dfs(0,0,best)
        #print(best)
        
        result = []
        mask = best[1]
        bit = 1
        i = n-1
        while i >= 0:
            if mask & bit:
                result.append(target[i])
                bit <<= 1
                i-=1
                
            else:
                cnt = 0
                while i >=0 and mask & bit == 0:
                    bit <<= 1
                    i-=1
                    cnt += 1
                result.append(str(cnt))
        
        ans = ""
        for x in reversed(result):
            ans += x
        return ans
