/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    private:
    int id = 0;
    public:
    TreeNode* helperForTree(vector<int>& in, vector<int>& post, int sidx, int eidx, unordered_map<int, int> &umap) {
        if(sidx > eidx) return nullptr;
        
        int val = post[id--];
        TreeNode* node = new TreeNode(val);

        int temp = umap[val];
    
        node->right = helperForTree(in, post, temp+1, eidx, umap);
        node->left = helperForTree(in, post, sidx, temp-1, umap);

        return node;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> umap;
        int n = inorder.size();
        for(int i = 0; i < n; i++) {
            umap[inorder[i]] = i;
        }
        id = n-1;
        return helperForTree(inorder, postorder, 0, n-1, umap);
    }
};
