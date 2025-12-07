class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int m = Math.min(sides[0], sides[1]);
        int M = Math.max(sides[0], sides[1]);
        int sh = M - m;
        int lo = M + m;
        for (int i = sh + 1; i < lo; i++) {answer++;}
        return answer;
    }
}