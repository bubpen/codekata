class Solution {
    public String solution(String polynomial) {
        String[] terms = polynomial.split(" \\+ ");
        int x_num = 0;
        int num = 0;
        for (String term : terms) {
            if (term.contains("x")) {
                if (term.equals("x")) {x_num++;}
                else {
                    String coefficientStr = term.replace("x", "");
                    x_num += Integer.parseInt(coefficientStr);
                    }
                } else {num += Integer.parseInt(term);}
            }
        StringBuilder answer = new StringBuilder();
        if (x_num != 0) {
            if (x_num == 1) {
                answer.append("x");
            } else {
                answer.append(String.valueOf(x_num)).append("x");
            }
        }
        if (num != 0) {
            if (x_num != 0) {
                answer.append(" + ");
            }
            answer.append(num);
        }
        if (answer.length() == 0) {
            return "0";
        }
        return answer.toString();
    }
}