class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int m = Integer.MIN_VALUE;
        for (int side : sides) {
            m = Math.max(m, side);
        }
        int total = 0;
        for (int side : sides) {
            total += side;
        }
        total -= m;
        if (total > m) {
            answer = 1;
        } else {answer = 2;}
        return answer;
    }
}