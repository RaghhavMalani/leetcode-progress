class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        const int MAX_VALUE = 200;

        vector<vector<int>> dp(
            MAX_VALUE + 1,
            vector<int>(MAX_VALUE + 1, 0)
        );

        dp[0][0] = 1;

        for (int x : nums) {
            vector<vector<int>> next(
                MAX_VALUE + 1,
                vector<int>(MAX_VALUE + 1, 0)
            );

            for (int gcd1 = 0; gcd1 <= MAX_VALUE; gcd1++) {
                for (int gcd2 = 0; gcd2 <= MAX_VALUE; gcd2++) {
                    if (dp[gcd1][gcd2] == 0) {
                        continue;
                    }

                    int ways = dp[gcd1][gcd2];

                    next[gcd1][gcd2] =
                        (next[gcd1][gcd2] + ways) % MOD;

                    int newGcd1 = gcd(gcd1, x);
                    next[newGcd1][gcd2] =
                        (next[newGcd1][gcd2] + ways) % MOD;

                    int newGcd2 = gcd(gcd2, x);
                    next[gcd1][newGcd2] =
                        (next[gcd1][newGcd2] + ways) % MOD;
                }
            }

            dp = move(next);
        }

        int answer = 0;

        for (int gcdValue = 1; gcdValue <= MAX_VALUE; gcdValue++) {
            answer = (answer + dp[gcdValue][gcdValue]) % MOD;
        }

        return answer;
    }
};