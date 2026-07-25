class Solution {
    private void backtrack(Integer start, List<Integer> comb, List<List<Integer>> res, Integer n, Integer k ){
        if (comb.size() == k){
            res.add(new ArrayList<>(comb));
            return;
        }

        for (Integer i = start; i <= n; i++){
            comb.add(i);
            backtrack(i+1, comb, res, n, k);
            comb.remove(comb.size() - 1);
        }
    }

    public List<List<Integer>> combine(Integer n, Integer k) {
        List<Integer> comb = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        backtrack(1,comb,res,n,k);
        return res;
    }
}


