#include <iostream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *right;
    TreeNode *left;
    TreeNode(int x): val(x), right(NULL), left(NULL) {}
};

class Solution
{
public:
    TreeNode *mirrorTree(TreeNode *root)
    {
        TreeNode *new_root = new TreeNode(0);
        if (root == NULL)
            return NULL;
        new_root->val = root->val;
        new_root->right = mirrorTree(root->left);
        new_root->left = mirrorTree(root->right);

        return new_root;
    }
};

int main()
{
    return 0;
}