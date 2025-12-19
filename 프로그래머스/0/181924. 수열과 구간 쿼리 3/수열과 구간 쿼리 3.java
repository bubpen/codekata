class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            answer[i] = arr[i];
        }
        for (int[] query : queries) {
            int a = query[0];
            int b = query[1];
            int save = answer[a];
            answer[a] = answer[b];
            answer[b] = save;
        }
        return answer;
    }
}