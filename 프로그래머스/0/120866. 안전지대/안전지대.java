class Solution {
    public int solution(int[][] board) {
        int len = board.length;
        int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
        int answer = 0;
    
        int[][] danger = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (board[i][j] == 1) {
                    danger[i][j] = 1;
                    for (int k = 0; k < 8; k++) {
                        int x = i + dx[k];
                        int y = j + dy[k];
                        if (0 <= x && x < len && 0 <= y && y < len) {
                            danger[x][y] = 1;
                        }
                    }
                }
            }
        }
        for (int x = 0; x < len; x++) {
            for (int y = 0; y < len; y++) {
                if (danger[x][y] == 0) {answer++;}
            }
        }
        return answer;
    }
}