#include <iostream>
#include <vector>
#include <stack>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
    public: 
        vector<int> reversed;
        void getNum(ListNode* p) {
            if(p != NULL) {
                getNum(p->next);
                reversed.push_back(p->val);
            }
        }
        vector<int> reverseList(ListNode* head) {
            
            getNum(head);
            return reversed;
        }
        vector<int> reverseList_stack(ListNode* head) {
            vector<int> reversed;
            stack<int> aux_stack;
            while(head != NULL) {
                aux_stack.push(head->val);
                head = head->next;
            }
            while(!aux_stack.empty()) {
                reversed.push_back(aux_stack.top());
                aux_stack.pop();
            }
            return reversed;
        }

};

int main() {
    // head: [1, 2, 3, 4]
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    Solution* s = new Solution();
    vector<int> list = s->reverseList_stack(head);

    for(unsigned long i=0; i<list.size(); i++) {
        cout<<list[i]<<" ";
    }
    return 0;
}
