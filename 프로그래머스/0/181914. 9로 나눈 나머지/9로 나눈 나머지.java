class Solution {
    public int solution(String number) {
        int total= 0;
        char[] nums = number.toCharArray();
        for (char num : nums) {
            total += num - '0';
        }
        return total % 9;
    }
}