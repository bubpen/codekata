class Solution {
    public int solution(int[] numbers) {
        int max = 0;
        int sub_max = 0;
        int max_index = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
                max_index = i;
            }
        }
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] > sub_max && i != max_index) {
                sub_max = numbers[i];
            }
        }
        int answer = max * sub_max;
        return answer;
    }
}