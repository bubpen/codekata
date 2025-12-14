class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        int complex = 1;
        for (int idx = 0; idx < num_list.length; idx++) {
            complex *= num_list[idx];
            sum += num_list[idx];
        }
        if ((int)Math.pow(sum, 2) > complex) {
            answer = 1;
        } else {answer = 0;}
        return answer;
    }
}