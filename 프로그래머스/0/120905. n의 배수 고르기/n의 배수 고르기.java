import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < numlist.length; i++) {
            if (numlist[i] % n == 0) {
                answer.add(numlist[i]);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}