#include <iostream>
#include <vector>
#include <queue>
#include <stack>
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
    vector<vector<int>> levelOrder2(TreeNode *root)
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

    vector<vector<int> >levelOrder(TreeNode *root)
    {
        vector<vector<int> > output;
        if (root == NULL)
            return output;
        
        stack<TreeNode *> tree_stack_lr, tree_stack_rl;

        int layer = 1;
        tree_stack_lr.push(root);
        while ((!tree_stack_lr.empty()) || (!tree_stack_rl.empty()))
        {
            vector<int> sub_output;
            if (layer%2 == 1)
                for (int i=tree_stack_lr.size(); i>0; i--)
                {
                    TreeNode *tree_node = tree_stack_lr.top();
                    tree_stack_lr.pop();
                    sub_output.push_back(tree_node->val);

                    if (tree_node->left != NULL)
                        tree_stack_rl.push(tree_node->left);
                    
                    if (tree_node->right != NULL)
                        tree_stack_rl.push(tree_node->right);
                }
            else                
                for (int i=tree_stack_rl.size(); i>0; i--)
                {
                    TreeNode *tree_node = tree_stack_rl.top();
                    tree_stack_rl.pop();
                    sub_output.push_back(tree_node->val);

                    if (tree_node->right != NULL)
                        tree_stack_lr.push(tree_node->right);

                    if (tree_node->left != NULL)
                        tree_stack_lr.push(tree_node->left);                        

                }
            layer += 1;
            output.push_back(sub_output);
        }
        return output;

        
    }
};

int main()
{
    return 0;
}