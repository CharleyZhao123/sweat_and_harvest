#include <iostream>
#include <vector>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution
{
    bool isMirror(TreeNode *A, TreeNode *B)
    {
        if (A == NULL && B == NULL)
            return true;
        else if (A == NULL || B == NULL)
            return false;

        if (A->val != B->val)
            return false;
        
        return (isMirror(A->left, B->right) && isMirror(A->right, B->left));
    }
    bool isSymmetric(TreeNode *root)
    {
        if (root == NULL)
            return true;
        return isMirror(root->left, root->right);
    }
    
};

int main()
{
    return 0;
}