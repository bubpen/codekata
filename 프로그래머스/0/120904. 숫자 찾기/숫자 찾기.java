class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        char[] nums = Integer.toString(num).toCharArray();      
        for (int i = 0; i < nums.length; i++) {
            int digit = nums[i] - '0';
            if (digit == k) {
                answer = i+1;
                break;
            }
        }
        return answer;
    }
}