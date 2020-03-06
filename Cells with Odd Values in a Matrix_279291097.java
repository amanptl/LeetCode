class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int[][] matrix = new int[n][m];
        int count = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                matrix[i][j] = 0;
            }
        }
        
        for(int i = 0; i < indices.length; i++){
            int row = indices[i][0];
            int col = indices[i][1];
            
            for (int j = 0; j < matrix[row].length; j++)
                matrix[row][j] +=1;
            for (int k = 0; k < matrix.length; k++)
                matrix[k][col] += 1;
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(matrix[i][j] % 2 != 0)
                    count++;
            }
        }
        
        return count;
    }
}
