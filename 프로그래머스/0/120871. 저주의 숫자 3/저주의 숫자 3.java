class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 1;
        while (i <= n) {
            answer++;
            String num = Integer.toString(answer);
            while (num.contains("3") || answer % 3 == 0) {
                answer++;
                num = Integer.toString(answer);
            }
            i++;
        }
        return answer;
    }
}