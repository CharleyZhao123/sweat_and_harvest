#include <iostream>
using namespace std;
// 递归经典题, 树先序遍历
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};
class Solution
{
public:
    bool sameRootStructure(TreeNode *A, TreeNode *B)
    {
        if (B == NULL)
            return true;
        if (A == NULL)
            return false;
        if (A->val != B->val)
            return false;
        return (sameRootStructure(A->left, B->left) && sameRootStructure(A->right, B->right));
    }
    bool isSubStructure(TreeNode *A, TreeNode *B)
    {
        if (A==NULL || B == NULL)
            return false;
        
        return (sameRootStructure(A, B) || isSubStructure(A->left, B) || isSubStructure(A->right, B));
    }
};

int main()
{
    return 0;
}