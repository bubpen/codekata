import java.util.HashMap;
class Solution {
    public String solution(int age) {
        HashMap<String, String> change = new HashMap<>();
        change.put("0", "a");
        change.put("1", "b");
        change.put("2", "c");
        change.put("3", "d");
        change.put("4", "e");
        change.put("5", "f");
        change.put("6", "g");
        change.put("7", "h");
        change.put("8", "i");
        change.put("9", "j");
        String before_age = Integer.toString(age);
        String answer = "";
        for (int i = 0; i < before_age.length(); i++) {
            String age_key = String.valueOf(before_age.charAt(i));
            answer = answer + change.get(age_key);
        }
        return answer;
    }
}