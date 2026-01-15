class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int sigma = 0;
        for (int i = 1; i < num; i++) {
            sigma += i;
        }
        int start = (total - sigma) / num;
        for (int i = 0; i < num; i++) {
            answer[i] = start + i;
        }
        return answer;
    }
}