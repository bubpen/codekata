class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int len = common.length - 1;
        if (common[2] - common[1] == common[1] - common[0]) {
            answer = common[len] + (common[2] - common[1]);
        } else {
            answer = common[len] * (common[2] / common[1]);
        }
        return answer;
    }
}