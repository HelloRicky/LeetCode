public class Solution {
    public int islandPerimeter(int[][] grid) {
        // p = island * 4 - nexter * 2
        
        int island = 0;
        int nexter = 0;
       for(int i = 0; i < grid.length; i++){
           for(int j = 0; j < grid[i].length; j++){
               if(grid[i][j] == 1){
                    island += 1;
                    if(i < grid.length - 1 && grid[i+1][j]==1) nexter += 1;
                    if(j < grid[i].length - 1 && grid[i][j+1]==1) nexter += 1;
               } 
               
           }
       }
       return island * 4 - nexter * 2;
    }
}