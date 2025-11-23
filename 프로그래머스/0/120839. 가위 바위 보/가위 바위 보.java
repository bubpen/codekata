class Solution {
    public String solution(String rsp) {
        String answer = "";
        for (char sequence : rsp.toCharArray()) {
            if (sequence == '0') {
                answer = answer + "5";
            } else if (sequence == '2') {
                answer = answer + "0";
            } else {
                answer = answer + "2";
            }
        }
        return answer;
    }
}