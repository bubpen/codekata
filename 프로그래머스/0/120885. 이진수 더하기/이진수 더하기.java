class Solution {
    public String solution(String bin1, String bin2) {
        String answer = "";
        int len1 = bin1.length() - 1;
        int len2 = bin2.length() - 1;
        int num1 = 0;
        int num2 = 0;
        for (char i : bin1.toCharArray()) {
            num1 += Character.getNumericValue(i) * Math.pow(2, len1);
            len1 -= 1;
        }
        for (char i : bin2.toCharArray()) {
            num2 += Character.getNumericValue(i) * Math.pow(2, len2);
            len2 -= 1;
        }
        int total = num1 + num2;
        answer = Integer.toBinaryString(total);
        return answer;
    }
}