class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        for (int i = 0; i < my_strings.length; i++) {
            int[] idx = parts[i];
            int s = idx[0];
            int f = idx[1];
            answer += my_strings[i].substring(s, f+1);
        }
        return answer;
    }
}