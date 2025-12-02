import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        my_string = my_string.toLowerCase();
        char[] char_array = my_string.toCharArray();
        Arrays.sort(char_array);
        String answer = new String(char_array);
        return answer;
    }
}