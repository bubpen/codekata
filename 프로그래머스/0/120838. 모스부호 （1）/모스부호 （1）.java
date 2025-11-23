import java.util.HashMap;
import static java.util.Map.entry;
import java.util.Map;

class Solution {
    public String solution(String letter) {
        String answer = "";
        HashMap<String, String> translation = new HashMap<>(
        Map.ofEntries(
        entry(".-", "a"), entry("-...", "b"), entry("-.-.", "c"), 
        entry("-..", "d"), entry(".", "e"), entry("..-.", "f"),
        entry("--.", "g"), entry("....", "h"), entry("..", "i"),
        entry(".---", "j"), entry("-.-", "k"), entry(".-..", "l"),
        entry("--", "m"), entry("-.", "n"), entry("---", "o"),
        entry(".--.", "p"), entry("--.-", "q"), entry(".-.", "r"),
        entry("...", "s"), entry("-", "t"), entry("..-", "u"),
        entry("...-", "v"), entry(".--", "w"), entry("-..-", "x"), entry("-.--", "y"), entry("--..", "z")));
        String[] word = letter.split(" ");
        String alphabet = "";
        for (String w : word) {
            alphabet = translation.get(w);
            answer = answer + alphabet;
        }
        return answer;
    }
}