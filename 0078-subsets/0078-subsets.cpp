class Solution {
private:
    void dfs(int i, vector<int>& nums, vector<vector<int>>& res, vector<int> &subset){
        if (i >= nums.size()){
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        dfs(i + 1, nums, res, subset);

        subset.pop_back();
        dfs(i + 1, nums, res, subset);
    }

public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        dfs(0,nums,res,subset);
        return res;
    }
};