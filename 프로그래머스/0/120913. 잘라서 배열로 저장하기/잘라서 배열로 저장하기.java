import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String my_str, int n) {
        List<String> answer = new ArrayList<>();
        StringBuilder word = new StringBuilder();
        char[] str = my_str.toCharArray();
        for (int i = 0; i < str.length; i++) {
            word.append(str[i]);
            if (word.length() == n || i == str.length - 1) {
                answer.add(word.toString());
                word.setLength(0);
            }
        }
        return answer.toArray(new String[0]);
    }
}