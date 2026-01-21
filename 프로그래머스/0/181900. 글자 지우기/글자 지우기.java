class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        char[] string = my_string.toCharArray();
        for (int i : indices) {
            string[i] = ' ';
        }
        for (char c : string) {
            if (c == ' ') {
                continue;
            }
            answer += c;
        }
        return answer;
    }
}