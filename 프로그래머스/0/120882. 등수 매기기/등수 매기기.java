import java.util.Arrays;
import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        Double[] averages = new Double[score.length];
        for (int i = 0; i < score.length; i++) {
            averages[i] = (score[i][0] + score[i][1]) / 2.0;
        }
        Double[] sorted = averages.clone();
        Arrays.sort(sorted, Collections.reverseOrder());
        for (int i = 0; i < score.length; i++) {
            for (int j = 0; j < score.length; j++) {
                if (averages[i].equals(sorted[j])) {
                    answer[i] = j + 1;
                    break;
                }
            }
        }
        return answer;
    }
}