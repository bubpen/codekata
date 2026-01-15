class Solution {
    public int solution(int M, int N) {
        int cnt_m = 0;
        int cnt_n = 0;
        while (M > 1) {
            cnt_m++;
            M--;
        }
        while (N > 1) {
            cnt_n++;
            N--;
        }
        int answer = cnt_m + (cnt_m + 1) * cnt_n;
        return answer;
    }
}