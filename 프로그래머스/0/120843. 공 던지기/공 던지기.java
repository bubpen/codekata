class Solution {
    public int solution(int[] numbers, int k) {
        int count = 0;
        int len = numbers.length;
        int answer = 0;
        while (len < 2 * k) {
            len += len;
        }
        int[] new_numbers = new int[len];
        for (int i = 0; i < len; i++) {
            new_numbers[i] = numbers[i % numbers.length];
        }
        for (int i = 0; i < len; i += 2) {
            answer = new_numbers[i];
            count++;
            if (count == k) {break;}
        }
        return answer;
    }
}