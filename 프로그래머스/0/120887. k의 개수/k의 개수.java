class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int num = i; num <= j; num++) {
            String number = "" + num;
            for (char c : number.toCharArray()) {
                if (Character.getNumericValue(c) == k) {
                    answer++;
                }
            }
        }
        return answer;
    }
}