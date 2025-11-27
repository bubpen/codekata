class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] strs = s.split(" ");
        for (int i = 0; i < strs.length; i++) {
            String str = strs[i];
            if (str.equals("Z")) {
                answer -= Integer.parseInt(strs[i-1]);
            } else {
                answer += Integer.parseInt(str);
            }
        }
        return answer;
    }
}