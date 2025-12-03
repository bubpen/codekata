class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for (int num : array) {
            String digit = Integer.toString(num);
            for(char c : digit.toCharArray()) {
                if (c == '7') {answer++;}
            }
        }
        return answer;
    }
}