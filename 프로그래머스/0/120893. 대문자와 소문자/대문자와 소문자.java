class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (char letter : my_string.toCharArray()) {
            if (Character.toUpperCase(letter) == letter) {
                answer += Character.toLowerCase(letter);
            } else {answer += Character.toUpperCase(letter);}
        }
        return answer;
    }
}