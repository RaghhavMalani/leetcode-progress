class Solution {
    private int dfs(int i, int total, int [] nums){
        if (i == nums.length){
            return total;
        }
        return dfs(i + 1, nums[i] ^ total, nums) + dfs(i + 1, total, nums);
    }

    public int subsetXORSum(int[] nums) {
        return dfs(0,0,nums);
    }
}