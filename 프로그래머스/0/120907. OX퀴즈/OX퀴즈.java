class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for (int i = 0; i < quiz.length; i++) {
            String[] c = quiz[i].split(" ");
            int num1 = Integer.parseInt(c[0]);
            int num2 = Integer.parseInt(c[2]);
            int expected = Integer.parseInt(c[4]);
            if (c[1].equals("+")) {
                if (num1 + num2 == expected) {
                    answer[i] = "O";
                } else {answer[i] = "X";}
            } else {
                if (num1 - num2 == expected) {
                    answer[i] = "O";
                } else {answer[i] = "X";}
            }
        }
        return answer;
    }
}