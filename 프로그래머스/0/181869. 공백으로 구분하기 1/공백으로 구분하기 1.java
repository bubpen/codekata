class Solution {
    public String[] solution(String my_string) {
        int count = 1;
        for (char c : my_string.toCharArray()) {
            if (c == ' ') {
                count++;
            }
        }
        String[] answer = new String[count];
        StringBuffer word = new StringBuffer();
        int idx = 0;
        for (char c : my_string.toCharArray()) {
            if (c == ' ') {
                answer[idx] = word.toString();
                idx++;
                word.setLength(0);
            } else {
                word.append(c);
            }
        }
        answer[idx] = word.toString();
        return answer;
    }
}