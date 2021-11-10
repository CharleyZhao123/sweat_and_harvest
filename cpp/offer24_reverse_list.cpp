#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        //三指针法
        ListNode *bp = NULL;
        ListNode *p = head;
        ListNode *ap = NULL;
        while (p != NULL)
        {
            ap = p->next;
            p->next = bp;

            bp = p;
            p = ap;
        }

        return bp;
    }

    ListNode *reverseList_recursion(ListNode *head)
    {
        //递归
        if (!head || !head->next)
        {
            return head;
        }
        ListNode *new_head = reverseList_recursion(head->next);
        head->next->next = head;
        head->next = NULL;

        return new_head;
    }
};

int main()
{
    ListNode *head = new ListNode(0);
    head->next = new ListNode(1);
    head->next->next = new ListNode(2);
    head->next->next->next = new ListNode(3);
    Solution *s = new Solution();

    ListNode *reversed_head = s->reverseList_recursion(head);

    while (reversed_head != NULL)
    {
        cout<<reversed_head->val<<" ";
        reversed_head = reversed_head->next;
    }

    return 0;
}
