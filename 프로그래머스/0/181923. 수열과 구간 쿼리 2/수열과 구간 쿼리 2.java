class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int s = query[0];
            int e = query[1];
            int k = query[2];
            int result = -1;
            for (int j = s; j <= e; j++) {
                if (arr[j] > k) {
                    if (result == -1) {
                        result = arr[j];
                    } else {
                        result = Math.min(arr[j], result);
                    }
                }
            }
            answer[i] = result;
        }
        return answer;
    }
}