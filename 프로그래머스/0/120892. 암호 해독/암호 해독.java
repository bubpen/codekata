class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        char[] sent = cipher.toCharArray();
        for (int i = code -1; i < cipher.length(); i += code) {
            answer += sent[i];
        }
        return answer;
    }
}