# 308. Range Sum Query 2D - Mutable
# Hard
# 30948FavoriteShare
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# 1.  The matrix is only modifiable by the update function.
# 2.  You may assume the number of calls to update and sumRegion function is distributed evenly.
# 3.  You may assume that row1 ≤ row2 and col1 ≤ col2.
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
        h = len(self.data)
        if h == 0: 
            self.tree = []
            return
        w = len(self.data[0])
        
        goal = max(h,w)
        curr = 1
        while curr < goal: curr *= 2
        
        self.tree = [0]*(curr*curr+curr*curr//2)
        
        def build_tree(tree,data,wl,wr,hl,hr,current):
            if wl == wr and hl == hr:
                #print(wl,hl,current)
                tree[current] = data[hl][wl]
                return data[hl][wl]
            elif wl == wr:
                hmid = (hl+hr)//2
                a = build_tree(tree,data,wl,wr,hl,hmid,current*4+1)
                b = build_tree(tree,data,wl,wr,hmid+1,hr,current*4+3)
                tree[current] = a+b
                return a+b
            elif hl == hr:
                wmid = (wl+wr)//2
                a = build_tree(tree,data,wl,wmid,hl,hr,current*4+1)
                b = build_tree(tree,data,wmid+1,wr,hl,hr,current*4+2)
                tree[current] = a+b
                return a+b
            else:
                hmid = (hl+hr)//2
                wmid = (wl+wr)//2
                a = build_tree(tree,data,wl,wmid,hl,hmid,current*4+1)
                b = build_tree(tree,data,wmid+1,wr,hl,hmid,current*4+2)
                c = build_tree(tree,data,wl,wmid,hmid+1,hr,current*4+3)
                d = build_tree(tree,data,wmid+1,wr,hmid+1,hr,current*4+4)
                tree[current] = a+b+c+d
                return a+b+c+d
        build_tree(self.tree,self.data,0,w-1,0,h-1,0)
        #print(self.tree)
        

    def update(self, row: int, col: int, val: int) -> None:
        def change(tree,diff,w_goal,h_goal,wl,wr,hl,hr,current):
            tree[current] += diff
            if w_goal == wl and w_goal == wr and h_goal == hl and h_goal == hr: return
            elif wl == wr:
                hmid = (hl+hr)//2
                if h_goal <= hmid: change(tree,diff,w_goal,h_goal,wl,wr,hl,hmid,current*4+1)
                else: change(tree,diff,w_goal,h_goal,wl,wr,hmid+1,hr,current*4+3)
            elif hl == hr:
                wmid = (wl+wr)//2
                if w_goal <= wmid: change(tree,diff,w_goal,h_goal,wl,wmid,hl,hr,current*4+1)
                else: change(tree,diff,w_goal,h_goal,wmid+1,wr,hl,hr,current*4+2)
            else:
                hmid = (hl+hr)//2
                wmid = (wl+wr)//2
                if h_goal <= hmid:
                    if w_goal <= wmid:change(tree,diff,w_goal,h_goal,wl,wmid,hl,hmid,current*4+1)
                    else:change(tree,diff,w_goal,h_goal,wmid+1,wr,hl,hmid,current*4+2)
                else:
                    if w_goal <= wmid:change(tree,diff,w_goal,h_goal,wl,wmid,hmid+1,hr,current*4+3)
                    else:change(tree,diff,w_goal,h_goal,wmid+1,wr,hmid+1,hr,current*4+4)
        
        diff = val - self.data[row][col]
        self.data[row][col] = val
        h = len(self.data)
        w = len(self.data[0])
        change(self.tree,diff,col,row,0,w-1,0,h-1,0)
        #print(self.tree)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def get(tree,row1,row2,col1,col2,wl,wr,hl,hr,current):
            if row1 == wl and row2 == wr and col1 == hl and col2 == hr: return tree[current]
            hmid = (hl+hr)//2
            wmid = (wl+wr)//2
            if row2 <= wmid:
                if col2 <= hmid:
                    return get(tree,row1,row2,col1,col2,wl,wmid,hl,hmid,current*4+1)
                elif col1 > hmid:
                    return get(tree,row1,row2,col1,col2,wl,wmid,hmid+1,hr,current*4+3)
                else:
                    a = get(tree,row1,row2,col1,hmid,wl,wmid,hl,hmid,current*4+1)
                    b = get(tree,row1,row2,hmid+1,col2,wl,wmid,hmid+1,hr,current*4+3)
                    return a + b
            elif row1 > wmid:
                if col2 <= hmid:
                    return get(tree,row1,row2,col1,col2,wmid+1,wr,hl,hmid,current*4+2)
                elif col1 > hmid:
                    return get(tree,row1,row2,col1,col2,wmid+1,wr,hmid+1,hr,current*4+4)
                else:
                    a = get(tree,row1,row2,col1,hmid,wmid+1,wr,hl,hmid,current*4+2)
                    b = get(tree,row1,row2,hmid+1,col2,wmid+1,wr,hmid+1,hr,current*4+4)
                    return a + b
            else:
                if col2 <= hmid:
                    a = get(tree,row1,wmid,col1,col2,wl,wmid,hl,hmid,current*4+1)
                    b = get(tree,wmid+1,row2,col1,col2,wmid+1,wr,hl,hmid,current*4+2)
                    return a + b
                elif col1 > hmid:
                    a = get(tree,row1,wmid,col1,col2,wl,wmid,hmid+1,hr,current*4+3)
                    b = get(tree,wmid+1,row2,col1,col2,wmid+1,wr,hmid+1,hr,current*4+4)
                    return a + b
                else:
                    a = get(tree,row1,wmid,col1,hmid,wl,wmid,hl,hmid,current*4+1)
                    b = get(tree,wmid+1,row2,col1,hmid,wmid+1,wr,hl,hmid,current*4+2)
                    c = get(tree,row1,wmid,hmid+1,col2,wl,wmid,hmid+1,hr,current*4+3)
                    d = get(tree,wmid+1,row2,hmid+1,col2,wmid+1,wr,hmid+1,hr,current*4+4)
                    return a+b+c+d
        h = len(self.data)
        w = len(self.data[0])
        return get(self.tree,col1,col2,row1,row2,0,w-1,0,h-1,0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
