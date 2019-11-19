# 272. Closest Binary Search Tree Value II
# Hard
# 41517FavoriteShare
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
# Note:
# •   Given target value is a floating point.
# •   You may assume k is always valid, that is: k ≤ total nodes.
# •   You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Example:
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: [4,3]
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
# Accepted
# 41,453
# Submissions
# 89,426
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def build_low_stack(root,target,stack):
            curr = root
            while curr != None:
                if curr.val == target: 
                    stack.append(curr)
                    break
                elif curr.val < target: 
                    stack.append(curr)
                    curr = curr.right
                else: curr = curr.left
        def build_high_stack(root,target,stack):
            curr = root
            while curr != None:
                if curr.val == target: 
                    stack.append(curr)
                    break
                elif curr.val > target: 
                    stack.append(curr)
                    curr = curr.left
                else: curr = curr.right
        def get_next_low(low_stack):
            result = low_stack.pop()
            curr = result.left
            while curr != None:
                low_stack.append(curr)
                curr = curr.right
            return result.val
        def get_next_high(high_stack):
            result = high_stack.pop()
            curr = result.right
            while curr != None:
                high_stack.append(curr)
                curr = curr.left
            return result.val
        
            
            
                    
        result = []
        low_stack = []
        high_stack = []
        build_low_stack(root,target,low_stack)
        build_high_stack(root,target,high_stack)
        #print(low_stack)
        #print(high_stack)
        if low_stack and high_stack and low_stack[-1] == high_stack[-1]:
            get_next_low(low_stack)
            
        while k:
            if len(low_stack) == 0:
                result.append(get_next_high(high_stack))
            elif len(high_stack) == 0:
                result.append(get_next_low(low_stack))
            else:
                #print(low_stack[-1].val,high_stack[-1].val)
                if abs(low_stack[-1].val-target) <= abs(high_stack[-1].val-target):
                    result.append(get_next_low(low_stack))
                else: 
                    result.append(get_next_high(high_stack))
                    #print(low_stack,high_stack)
            k -= 1
            #print(low_stack,high_stack)
        return result
