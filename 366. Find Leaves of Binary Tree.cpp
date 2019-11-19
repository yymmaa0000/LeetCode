// 366. Find Leaves of Binary Tree
// Medium
// 66410FavoriteShare
// Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
 
// Example:
// Input: [1,2,3,4,5]
  
//           1
//          / \
//         2   3
//        / \     
//       4   5    

// Output: [[4,5,3],[2],[1]]
 
// Explanation:
// 1. Removing the leaves [4,5,3] would result in this tree:
//           1
//          / 
//         2          
 
// 2. Now removing the leaf [2] would result in this tree:
//           1          
 
// 3. Now removing the leaf [1] would result in the empty tree:
//           []         
// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };
//  */
class Solution {
public:
    int dfs(TreeNode* root, vector<vector<int>> &result){
            if (root == NULL) return -1;
            int left = dfs(root->left,result);
            int right = dfs(root->right,result);
            int level = max(left,right)+1;
        if (level >= result.size()){
            result.push_back(vector<int>{root->val});
        }
        else {
            result[level].push_back(root->val);
        }
        
        return level;
    }
    
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> result;
        
        
        cout<<dfs(root,result);
        return result;
    }
};
