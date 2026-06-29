class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> stack;

        for(string op : operations){
            if (op == "+"){
                stack.push_back(stack.back() + stack[stack.size() -2]);
            }
            else if (op == "D"){
                stack.push_back(stack.back()*2);
            }
            else if (op == "C"){
                stack.pop_back();
            }
            else {
                stack.push_back(stoi(op));
            }
        }

        int sum = 0;
        for (int num : stack){
            sum += num;
        }

        return sum;
    }
};