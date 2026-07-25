class Solution {
    private void dfs(int i, int[] nums, int target, List<List<Integer>> res, List<Integer> curr, int total){
        if (total == target){
            res.add(new ArrayList<>(curr));
            return;
        }
        if (total > target || i >= nums.length){
            return;
        }

        curr.add(nums[i]);
        dfs(i,nums,target,res,curr, total + nums[i]);

        curr.remove(curr.size() - 1);
        dfs(i + 1,nums,target,res,curr, total);
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        dfs(0, nums, target, res, curr, 0);
        return res;   
    }
}
