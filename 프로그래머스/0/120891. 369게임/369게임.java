class Solution {
    public int solution(int order) {
        int answer = 0;
        String number = Integer.toString(order);
        for (char num : number.toCharArray()) {
            int digit = Character.getNumericValue(num);
            if (digit != 0 && digit % 3 == 0) {
                answer += 1;
            }
        }
        return answer;
    }
}