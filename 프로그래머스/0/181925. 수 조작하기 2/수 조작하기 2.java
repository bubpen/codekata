class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        for (int i = 1; i < numLog.length; i++) {
            int now = numLog[i];
            int before = numLog[i - 1];
            if (now - before == 1) {
                answer += "w";
            } else if (now - before == -1) {
                answer += "s";
            } else if (now - before == 10) {
                answer += "d";
            } else {answer += "a";}
        }
        return answer;
    }
}