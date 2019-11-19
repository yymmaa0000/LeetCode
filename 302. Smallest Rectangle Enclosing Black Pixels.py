# 302. Smallest Rectangle Enclosing Black Pixels
# Hard
# 15243FavoriteShare
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
# Example:
# Input:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2

# Output: 6
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def left_bs(image,l,r):
            while (r-l) > 1:
                mid = (l+r)//2
                found = False
                for i in range(len(image)):
                    if image[i][mid] == "1":
                        found = True
                        break
                if found: r = mid
                else: l = mid
            found = False
            for i in range(len(image)):
                if image[i][l] == "1":
                    found = True
                    break
            if found: return l
            else: return r
        def right_bs(image,l,r):
            while (r-l) > 1:
                mid = (l+r)//2
                found = False
                for i in range(len(image)):
                    if image[i][mid] == "1":
                        found = True
                        break
                if found: l = mid
                else: r = mid
            found = False
            for i in range(len(image)):
                if image[i][r] == "1":
                    found = True
                    break
            if found: return r
            else: return l
        def up_bs(image,l,r):
            while (r-l) > 1:
                mid = (l+r)//2
                found = False
                for i in range(len(image[0])):
                    if image[mid][i] == "1":
                        found = True
                        break
                if found: r = mid
                else: l = mid
            found = False
            for i in range(len(image[0])):
                if image[l][i] == "1":
                    found = True
                    break
            if found: return l
            else: return r
        def down_bs(image,l,r):
            while (r-l) > 1:
                mid = (l+r)//2
                found = False
                for i in range(len(image[0])):
                    if image[mid][i] == "1":
                        found = True
                        break
                if found: l = mid
                else: r = mid
            found = False
            for i in range(len(image[0])):
                #print(r,i)
                if image[r][i] == "1":
                    found = True
                    break
            if found: return r
            else: return l
        height = len(image)-1
        width = len(image[0])-1
        print(right_bs(image,y,width) )
        print(left_bs(image,0,y))
        print(down_bs(image,x,height))
        print(up_bs(image,0,x))
        return (right_bs(image,y,width) - left_bs(image,0,y)+1)*(down_bs(image,x,height) - up_bs(image,0,x)+1)
        
