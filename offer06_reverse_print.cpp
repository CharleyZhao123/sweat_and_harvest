#include <iostream>
#include <vector>
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

};

int main() {
    // head: [1, 2, 3, 4]
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    Solution* s = new Solution();
    vector<int> list = s->reverseList(head);

    for(unsigned long i=0; i<list.size(); i++) {
        cout<<list[i]<<" ";
    }
    return 0;
}
