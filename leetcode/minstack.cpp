#include <stack>

class MinStack {
private:
    std::stack<int> min{};
    std::stack<int> stack{};
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (min.empty() || val <= min.top()) {
            min.push(val);
        }
        stack.push(val);
    }
    
    void pop() {
        if (!stack.empty() && !min.empty() && stack.top() == min.top()) {
            min.pop();
        }

        stack.pop();
    }
    
    int top() {
        return stack.empty() ? 0 : stack.top();
    }
    
    int getMin() {
        return min.empty() ? 0 : min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */