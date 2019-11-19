# 1088. Confusing Number II
# Hard
# 175FavoriteShare
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)
# Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
 
# Example 1:
# Input: 20
# Output: 6
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
# Example 2:
# Input: 100
# Output: 19
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 
# Note:
# 1.  1 <= N <= 10^9
class Solution:
    def confusingNumberII(self, N: int) -> int:
        if N < 6: return 0
        if N < 9: return 1
        if N < 10: return 2
        
        N = str(N)
        n = len(N)
        
        # find all valid number with length < n
        result = 2
        for i in range(2,n):
            result += 4*(5**(i-1))
            if i % 2 == 1:
                result -= 3*4*(5**(i//2-1))
            else:
                result -= 4*(5**(i//2-1))
        
        '''def get_similar_num(i):
            # get the number of similar numbers with digit i
            # can start with 0
            if i == 1: return 5
            elif i % 2 == 1:
                return -= 3*4*(5**(i//2-1))
            else:
                result -= 4*(5**(i//2-1))'''
        
        # find all number with length = n, including strobographic number
        print(result)
        less = [1,2,2,2,2,2,3,3,4,5]
        valid = set([0,1,6,8,9])
        
        original_good = True
        for i in range(n):
            temp = 1
            x = int(N[i])
            if x == 0: continue
            if i == 0: temp *= less[x-1]-1
            else: temp *= less[x-1]
            temp *= 5**(n-i-1)
            result += temp
            if x not in valid: 
                original_good = False
                break
        if original_good: result += 1
        
                
        '''for key,val in enumerate(N):
            if key == 0: temp *= less[int(val)]-1
            else: temp *= less[int(val)]
            print(temp)
        result += temp'''
        
        
        # subtract the number of strobographic number with length = n
        dic = {'6': '9', '9': '6', '8': '8', '0': '0', '1': '1'}
        buf = collections.deque()

        def is_valid(buf):
            x = "".join(buf)
            return x <= N


        def make_strobo(buf,length):
            result = 0
            if len(buf) == length:
                if buf[0] != '0' and is_valid(buf):
                    result += 1
                return result
            elif len(buf) == length-1:
                for x in ('0','1','8'):
                    buf.insert(len(buf)//2,x)
                    if buf[0] != '0' and is_valid(buf):
                        result += 1
                    del buf[len(buf)//2]
                return result
            else:
                for x in dic:
                    buf.append(x)
                    buf.appendleft(dic[x])
                    result += make_strobo(buf,length)
                    buf.pop()
                    buf.popleft()
    #        print(result)
            return result
    
        print(result)
        result -= make_strobo(buf,n)
        return result
