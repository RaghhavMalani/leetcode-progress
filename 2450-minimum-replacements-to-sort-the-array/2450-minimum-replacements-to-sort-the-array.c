long long solve(int index, long long right_bound, int* nums) {
    if (index < 0) {
        return 0;
    }

    long long current_element = nums[index];

    if (current_element > right_bound) {
        long long k = (current_element + right_bound - 1) / right_bound;
        long long new_bound = current_element / k;
        return (k - 1) + solve(index - 1, new_bound, nums);
    } 
    
    return solve(index - 1, current_element, nums);
}

long long minimumReplacement(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return 0;
    }
    
    return solve(numsSize - 2, nums[numsSize - 1], nums);
}