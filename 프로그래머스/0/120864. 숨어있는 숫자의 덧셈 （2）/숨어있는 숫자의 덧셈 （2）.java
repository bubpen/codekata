class Solution {
    public int solution(String my_string) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        for (char c : my_string.toCharArray()) {
            if (Character.isDigit(c)) {
                sb.append(c);
            } else {sb.append(" ");}
        }
        String s = sb.toString();
        String[] nums = s.split("\\s+");
        for (String c : nums) {
            if (!c.isEmpty()) {
                answer += Integer.parseInt(c);
        
            }
        }
        return answer;
    }
}