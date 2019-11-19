# 248. Strobogrammatic Number III
# Hard
# 130118FavoriteShare
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
# Example:
# Input: low = "50", high = "100"
# Output: 3 
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.
# Note:
# Because the range might be a large number, the low and high numbers are represented as string.
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        if int(high) < int(low): return 0
        l = len(low)
        r = len(high)
        result = 0
        for i in range(l+1,r):
            if i%2:result += 3*4*(5**((i-3)//2))
            else: result += 4*(5**((i-2)//2))

        dic = {'6': '9', '9': '6', '8': '8', '0': '0', '1': '1'}
        buf = collections.deque()

        def is_valid(buf):
            x = "".join(buf)
    #        print(x)
            if l == r: return low <= x <= high
            elif len(x) == l: 
    #            print(x >= low)
                return x >= low
            elif len(x) == r: 
    #            print(x <= high)
                return x <= high
            return True

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

        result += make_strobo(buf,l)
        if r != l: result += make_strobo(buf,r)
        if low == "0": result += 1
        return result
