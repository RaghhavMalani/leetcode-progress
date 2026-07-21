class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int active = count(s.begin(), s.end(), '1');
        int previousZeros = -1;
        int currentZeros = 0;
        int maxGain = 0;

        for (char c : s) {
            if (c == '0') {
                currentZeros++;
            } else if (currentZeros > 0) {
                if (previousZeros != -1) {
                    maxGain = max(maxGain, previousZeros + currentZeros);
                }

                previousZeros = currentZeros;
                currentZeros = 0;
            }
        }

        if (currentZeros > 0 && previousZeros != -1) {
            maxGain = max(maxGain, previousZeros + currentZeros);
        }

        return active + maxGain;
    }
};