class Solution {
public:
    string smallestSubsequence(string s) {
        vector<int> last(26);
        vector<bool> used(26, false);

        for (int i = 0; i < s.size(); i++) {
            last[s[i] - 'a'] = i;
        }

        string result;

        for (int i = 0; i < s.size(); i++) {
            int current = s[i] - 'a';

            if (used[current]) {
                continue;
            }

            while (!result.empty() &&
                   result.back() > s[i] &&
                   last[result.back() - 'a'] > i) {
                used[result.back() - 'a'] = false;
                result.pop_back();
            }

            result.push_back(s[i]);
            used[current] = true;
        }

        return result;
    }
};