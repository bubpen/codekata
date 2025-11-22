import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        ArrayList<Integer> quick = new ArrayList<>();
        for (int val : emergency) {
            quick.add(val);
        }
        quick.sort(Comparator.reverseOrder());
        for (int i = 0; i < emergency.length; i++) {
            answer[i] = quick.indexOf(emergency[i]) + 1;
        }
        return answer;
    }
}