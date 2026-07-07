class Solution {
    public int subsetXORSum(int[] nums) {
        int res = 0;

        for (int n : nums) {
            res = res | n;
        }

        return res * (1 << (nums.length - 1));
    }
}