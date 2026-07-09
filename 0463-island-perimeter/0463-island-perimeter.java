class Solution {
    private int dfs(int i, int j, int[][]grid, Set<ArrayList<Integer>>visit){
        if (i >= grid.length || j >= grid[0].length || i < 0 || j < 0 ||grid[i][j] == 0){
            return 1;
        }
        ArrayList<Integer> pair = new ArrayList<>(List.of(i, j));
        if (visit.contains(pair)){
            return 0;
        }

        visit.add(pair);
        int perim = dfs(i+1,j,grid,visit);
        perim += dfs(i,j+1,grid,visit);
        perim += dfs(i-1,j,grid,visit);
        perim += dfs(i,j-1,grid,visit);
        return perim;
    }

    public int islandPerimeter(int[][] grid) {
        HashSet<ArrayList<Integer>> visit = new HashSet<>();
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] != 0){
                    return dfs(i,j,grid,visit);
                }
            }
        }
        return 0;
    }
}