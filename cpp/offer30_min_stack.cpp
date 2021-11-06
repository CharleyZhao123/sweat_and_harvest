#include <iostream>
#include <stack>
using namespace std;
class MinStack {
    private: stack<int> data_stack, aux_stack;
    public: 
        MinStack() {
            while(!data_stack.empty()) {
                data_stack.pop();
            }
            while(!aux_stack.empty()) {
                aux_stack.pop();
            }
        }
        void push(int x) {
            data_stack.push(x);
            if (!aux_stack.empty()) {
                if(x <= aux_stack.top()) {
                    aux_stack.push(x);
                }
            }
            else {
                aux_stack.push(x);
            }
        }
        void pop() {
            if(data_stack.top() == aux_stack.top()) {
                aux_stack.pop();
            }
            data_stack.pop();
        }
        int top() {
            return data_stack.top();
        }
        int min() {
            return aux_stack.top();
        }
};

int main() {
    MinStack* min_stack = new MinStack();
    min_stack->push(2);
    min_stack->push(4);
    min_stack->push(3);
    min_stack->push(1);
    min_stack->push(5);
    min_stack->pop();
    cout<<min_stack->min()<<endl;
    min_stack->pop();
    cout<<min_stack->min()<<endl;
    return 0;
}
