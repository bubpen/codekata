import java.util.Arrays;

class Solution {
    public int solution(String before, String after) {
        if (before.length() != after.length()) {return 0;}
        char[] c1 = before.toCharArray();
        char[] c2 = after.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
        int answer = 0;
        if (Arrays.equals(c1, c2)) {
            answer = 1;
        }
        return answer;
    }
}