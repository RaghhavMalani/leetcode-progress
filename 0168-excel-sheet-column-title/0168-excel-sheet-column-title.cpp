class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res = "";
        while(columnNumber > 0){
            int offset = (columnNumber - 1) % 26;
            res += (char)('A' + offset);
            columnNumber = (columnNumber - 1) / 26;   
        }
        reverse(res.begin(), res.end());
        return res;
    }
};