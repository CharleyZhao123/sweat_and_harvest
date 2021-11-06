#include <iostream>
#include <stack>
using namespace std;
class CQueue {
    private: stack<int> stack1, stack2;
    public:
        CQueue() {
            while(!stack1.empty()) {
                stack1.pop();
            }
            while(!stack2.empty()) {
                stack2.pop();
            }
        }
        
        void appendTail(int value) {
            stack1.push(value);
        }
        
        int deleteHead() {
            if(stack2.empty()) {
                if(stack1.empty()){
                    return -1;
                }
                else {
                    while(!stack1.empty()) {
                        // cout<<stack1.top();
                        stack2.push(stack1.top());
                        stack1.pop();
                    }
                }
            }
            int s2_top = stack2.top();
            stack2.pop();
            return s2_top;
        }
};

int main() {
    int value = 1;
    CQueue* obj = new CQueue();
    obj->appendTail(value);
    int param_2 = obj->deleteHead();
    cout<<param_2;
    return 0;
}
