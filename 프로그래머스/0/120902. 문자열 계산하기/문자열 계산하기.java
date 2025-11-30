class Solution {
    public int solution(String my_string) {
        String[] strs = my_string.split(" ");
        int answer = Integer.parseInt(strs[0]);
        for (int i = 2; i < strs.length; i += 2) {
            if (strs[i-1].equals("+")) {
                answer += Integer.parseInt(strs[i]);
            } else {
                answer -= Integer.parseInt(strs[i]);
            }
        }
        return answer;
    }
}