class Solution {
    public String solution(String str1, String str2) {
        StringBuilder answer = new StringBuilder();
        char[] char1 = str1.toCharArray();
        char[] char2 = str2.toCharArray();
        int len = char1.length;
        for (int i = 0; i < len; i++) {
            answer.append(char1[i]);
            answer.append(char2[i]);
        }
        return answer.toString();
    }
}