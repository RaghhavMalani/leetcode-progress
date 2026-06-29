class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String op: operations){
            if(op.equals("+")){
                int last = stack.get(stack.size() -1);
                int sec_last = stack.get(stack.size() -2);
                stack.push(last + sec_last);
            }
            else if (op.equals("D")){
                int last = stack.get(stack.size() -1);
                stack.push(2*last); //stack.push(stack.peek() * 2);
            }
            else if (op.equals("C")){
                stack.pop();
            }
            else{
                stack.push(Integer.parseInt(op));
            }
        }

        int score =0;
        for (int num: stack){
            score += num;
        }

        return score;
    }
}