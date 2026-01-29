import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> idx = new ArrayList();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                idx.add(i);
            }
        }
        if (idx.size() != 0) {
            int start = idx.get(0), end = idx.get(idx.size() -1);
            int[] answer = new int[end - start + 1];
            for (int i = start; i<= end; i++) {
                answer[i - start] = arr[i];
            }
            return answer;
        }
        int[] answer = new int[1];
        answer[0] = -1;
        return answer;
    }
}