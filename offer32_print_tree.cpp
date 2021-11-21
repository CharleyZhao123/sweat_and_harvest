#include <iostream>
#include <vector>
#include <queue>
using namespace std;
// 广度优先搜索二叉树: 借助队列先进先出的特点

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    vector<int> levelOrder1(TreeNode *root)
    {
        vector<int> output;
        if (root == NULL)
            return output;

        queue<TreeNode *> tree_queue;
        tree_queue.push(root);
        while (!tree_queue.empty())
        {
            TreeNode *tree_node = tree_queue.front();
            tree_queue.pop();

            output.push_back(tree_node->val);
            if (tree_node->left != NULL)
                tree_queue.push(tree_node->left);

            if (tree_node->right != NULL)
                tree_queue.push(tree_node->right);
        }
        return output;
    }
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int> > output;
        if (root == NULL)
            return output;
        
        queue<TreeNode *> tree_queue;
        tree_queue.push(root);


        while (!tree_queue.empty())
        {
            vector<int> sub_output;
            int size = tree_queue.size();
            for (int i=0; i<size; i++)
            {
                TreeNode *tree_node = tree_queue.front();
                tree_queue.pop();
                sub_output.push_back(tree_node->val);

                if (tree_node->left != NULL)
                    tree_queue.push(tree_node->left);
                if (tree_node->right != NULL)
                    tree_queue.push(tree_node->right);
            }
            output.push_back(sub_output);
        }
        return output;
    }
};

int main()
{
    return 0;
}