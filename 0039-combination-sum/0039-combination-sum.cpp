class Solution {
private:
    void dfs(int i, vector<int>& nums, int target, vector<vector<int>>& res, vector<int>& curr, int total){
        if (total == target){
            res.push_back(curr);
            return;
        }
        if (total > target || i >= nums.size()){
            return;
        }

        curr.push_back(nums[i]);
        dfs(i,nums,target,res,curr, total + nums[i]);

        curr.pop_back();
        dfs(i + 1,nums,target,res,curr, total);
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;;
        vector<int> curr;
        dfs(0, candidates, target, res, curr, 0);
        return res;
    }
};

