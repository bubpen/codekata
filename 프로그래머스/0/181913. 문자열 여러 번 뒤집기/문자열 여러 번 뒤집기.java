class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] letters = my_string.toCharArray();
        for (int[] index : queries) {
            int start = index[0];
            int end = index[1];
            while (start < end) {
                char temp = letters[start];
                letters[start] = letters[end];
                letters[end] = temp;
                start++;
                end--;
            }
        }
        String answer = "";
        for (char c : letters) {
            answer += c;
        }
        return answer;
    }
}