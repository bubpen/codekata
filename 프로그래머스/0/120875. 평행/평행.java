class Solution {
    public int solution(int[][] dots) {
        int[] x = new int[4];
        int[] y = new int[4];
        for (int i = 0; i < 4; i++) {
            x[i] = dots[i][0];
            y[i] = dots[i][1];
        }
        boolean answer1 = (y[0] - y[1]) * (x[2]-x[3]) == (y[2] - y[3]) * (x[0] - x[1]);
        boolean answer2 = (y[0] - y[2]) * (x[1]-x[3]) == (y[1] - y[3]) * (x[0] - x[2]);
        boolean answer3 = (y[0] - y[3]) * (x[1]-x[2]) == (y[1] - y[2]) * (x[0] - x[3]);
        if (answer1 || answer2 || answer3) {
            return 1;}
        return 0;
    }
}