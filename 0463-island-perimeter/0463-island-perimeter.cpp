class Solution {
private :
    int dfs(int i, int j, vector<vector<int>>& grid, set<vector<int>>& visit){
        if (i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0 ||grid[i][j] == 0){
            return 1;
        }
        if (visit.count({i, j})){
            return 0;
        }

        visit.insert({i, j});
        int perim = dfs(i+1,j,grid,visit);
        perim += dfs(i,j+1,grid,visit);
        perim += dfs(i-1,j,grid,visit);
        perim += dfs(i,j-1,grid,visit);
        return perim;
    }
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        set<vector<int>> visit;
        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] != 0){
                    return dfs(i,j,grid,visit);
                }
            }
        }
        return 0;
    }
};