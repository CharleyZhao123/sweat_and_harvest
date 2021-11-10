#include <iostream>
#include <map>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node *random;

    Node(int _val)
    {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        if (!head)
        {
            return NULL;
        }
        Node *new_head = new Node(head->val);
        Node *p_new = new_head;
        Node *p_old = head;

        map<Node *, int> path_i;
        map<int, Node *> i_path;

        int i = 0;
        path_i[head] = i;
        i_path[i] = new_head;

        while (p_old->next)
        {
            i += 1;
            p_old = p_old->next;
            path_i[p_old] = i;

            p_new->next = new Node(p_old->val);
            p_new = p_new->next;
            i_path[i] = p_new;
        }
        path_i[NULL] = -1;
        i_path[-1] = NULL;
        
        p_new = new_head;
        p_old = head;
        while (p_new)
        {
            p_new->random = i_path[path_i[p_old->random]];
            p_new = p_new->next;
            p_old = p_old->next;
        }
        
        return new_head;
    }
};

int main()
{
    int a = 0;
    cout<<!a<<endl;
    if (a)
    {
        cout<<666<<endl;
    }
    return 0;
}
