import java.util.HashMap;
import static java.util.Map.entry;
import java.util.Map;

class Solution {
    public long solution(String numbers) {
        String answer = "";
        HashMap<String, String> translation = new HashMap(
        Map.ofEntries(
        entry("one", "1"), entry("two", "2"), entry("three", "3"), entry("four", "4"), entry("five", "5"), entry("six", "6"), entry("seven", "7"), entry("eight", "8"), entry("nine", "9"), entry("zero", "0")));
        String word = "";
        for (char letter : numbers.toCharArray()) {
            word += letter;
            if (translation.containsKey(word)) {
                answer += translation.get(word);
                word = "";
            }
        }
        return Long.parseLong(answer);
    }
}