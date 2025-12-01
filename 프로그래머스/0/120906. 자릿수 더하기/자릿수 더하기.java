class Solution {
    public int solution(int n) {
        int answer = 0;
        char[] num = Integer.toString(n).toCharArray();
        for (char c : num) {
            int digit = c - '0';
            answer += digit;
        }
        return answer;
    }
}