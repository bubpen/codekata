import java.util.ArrayList;
import java.util.Comparator;
import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for (char word : my_string.toCharArray()) {
            if (Character.isDigit(word)) {
                int digit = Character.getNumericValue(word);
                numbers.add(digit);
            }
        }
        int[] answer = new int[numbers.size()];
        for (int i = 0; i < numbers.size(); i++) {
            answer[i] = numbers.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}