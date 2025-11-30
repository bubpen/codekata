import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        Set<String> sset = new HashSet<>(Arrays.asList(s1));
        for (String s : s2) {
            if (sset.contains(s)) {
                answer++;
            }
        }
        return answer;
    }
}