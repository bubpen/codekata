class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int max_x = dots[0][0];
        int min_x = dots[0][0];
        int max_y = dots[0][1];
        int min_y = dots[0][1];
        for (int[] point : dots) {
            min_x = Math.min(min_x, point[0]);
            max_x = Math.max(max_x, point[0]);
            min_y = Math.min(min_y, point[1]);
            max_y = Math.max(max_y, point[1]);
        }
        answer = Math.abs(max_x - min_x) * Math.abs(max_y - min_y);
        return answer;
    }
}