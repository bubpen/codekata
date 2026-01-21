import java.util.ArrayList;

class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        char[] strings = my_string.toCharArray();
        ArrayList<Character> reverse = new ArrayList<>();
        for (int i = s; i <= e; i++) {
            reverse.add(0, strings[i]);
        }
        for (int i = 0; i < reverse.size(); i++) {
            strings[i + s] = reverse.get(i);
        }
        for (char c : strings) {
            answer += c;
        }
        return answer;
    }
}