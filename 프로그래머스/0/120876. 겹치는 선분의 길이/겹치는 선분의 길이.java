class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        int[] count = new int[200];
        for (int[] dots : lines) {
            int start = dots[0];
            int end = dots[1];
            for (int i = start; i < end; i++) {
                count[i + 100]++;
            }
        }
        for (int i : count) {
            if (i > 1) {answer++;}
        }
        return answer;
    }
}