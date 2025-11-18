class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int index;
        double total = 0;
        for (index = 0; index < numbers.length; index++) {
            total = total + numbers[index];
        }
        answer = total / numbers.length; 
        return answer;
    }
}