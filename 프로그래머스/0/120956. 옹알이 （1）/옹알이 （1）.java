class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] baby = {"aya", "ye", "woo", "ma"};
        for (String word : babbling) {
            for (String b : baby) {
                if (word.contains(b)) {
                    word = word.replace(b, " ");
                    if (word.replace(" ", "").equals("")) {
                        answer += 1;
                        break;
                    }
                }
            }
        }
        return answer;
    }
}