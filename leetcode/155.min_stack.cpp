class MinStack {
public:
    long data[10000];
    int top_p = -1;
    long min = 0;
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if (top_p<0)
            min = x;
        data[++top_p] = x - min;
        if (x<min)
            min = x;
    }
    
    void pop() {
        if (top_p<0)
            return;
        long d = data[top_p--];
        if (d<0) {
            min -= d;
        }
    }
    
    int top() {
        long d=data[top_p];
        return d<0 ? min:d+min;
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
