class Solution {
    public int[] solution(int[] num_list) {
        int last_index = num_list.length - 1;
        int[] answer = new int[last_index + 2];
        for (int i = 0; i < answer.length; i++) {
            if (i == answer.length - 1) {
                if (num_list[last_index] > num_list[last_index - 1]) {
                    answer[i] = num_list[last_index] - num_list[last_index - 1];
                } else {
                    answer[i] = 2 * num_list[last_index];
                }
            } else {
                answer[i] = num_list[i];
            }
        } 
        return answer;
    }
}