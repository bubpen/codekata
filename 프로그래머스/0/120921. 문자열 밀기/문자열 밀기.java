class Solution {
    public int solution(String A, String B) {
        int answer = -1;
        if (A.equals(B)) {
            answer = 0;
        } else {
            int len = A.length();
            for (int i = 1; i < len; i++) {
                A = A.substring(len-1) + A.substring(0, len -1);
                if (A.equals(B)) {
                    answer = i;
                    break;
                }
            }
        }
        return answer;
    }
}