import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList();
        for (int i = l; i <= r; i++) {
            boolean yes = true;
            for (char c : Integer.toString(i).toCharArray()) {
               if (c == '0' || c == '5') {
                   continue;
               } else {
                   yes = false;
                   break;
               }
            }
            if (yes) {
                answer.add(i);
            }
        }
        if (answer.isEmpty()) {
            return new int[]{-1};
        }
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}