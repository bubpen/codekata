import java.util.TreeMap;
class Solution {
    public String solution(String s) {
        String answer = "";
        TreeMap<Character, Integer> count = new TreeMap<>();
        for (char c : s.toCharArray()) {
            if (count.containsKey(c)) {
                count.put(c, count.get(c) + 1);
            } else {
                count.put(c,1);
            }
        }
        for (char c : count.keySet()) {
            if (count.get(c) == 1) {
                answer += c;
            }
        }
        return answer;
    }
}