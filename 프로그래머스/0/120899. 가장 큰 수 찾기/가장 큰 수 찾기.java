class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int mx = array[0];
        int mn = array[0];
        int ind = 0;
        for (int i = 1; i < array.length; i++) {
            if (mx < array[i]) {
                mx = array[i];
                ind = i;
            }
        }
        answer[0] = mx;
        answer[1] = ind;
        return answer;
    }
}