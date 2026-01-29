import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        ArrayList<Integer> answer = new ArrayList();
        for (int[] idx : intervals) {
            int start = idx[0];
            int end = idx[1];
            for (int i = start; i <= end; i++) {
                answer.add(arr[i]);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}