class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        int near_diff = Math.abs(answer - n);
        int diff = 0;
        for (int i : array) {
            diff = Math.abs(i - n);
            if (diff < near_diff) {
                answer = i;
                near_diff = diff;
            } else if (diff == near_diff) {
                if (i < answer) {answer = i;}
            }
        }
        return answer;
    }
}