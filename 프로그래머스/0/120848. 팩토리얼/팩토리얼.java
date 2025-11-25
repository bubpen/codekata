class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = 1;
        int sup = 1;
        while (true) {
            sup *= num;
            num++;
            if (sup == n || n - (sup * num)  < 0) {
                answer = num - 1;
                break;
            }
        }
        return answer;
    }
}