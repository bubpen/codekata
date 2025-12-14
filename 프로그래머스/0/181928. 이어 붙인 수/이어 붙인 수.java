class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String even = "";
        String odd = "";
        for (int idx = 0; idx < num_list.length; idx++) {
            if (num_list[idx] % 2 == 0) {
                even += String.valueOf(num_list[idx]);
            } else {odd += String.valueOf(num_list[idx]);}
        }
        answer = Integer.parseInt(even) + Integer.parseInt(odd);
        return answer;
    }
}