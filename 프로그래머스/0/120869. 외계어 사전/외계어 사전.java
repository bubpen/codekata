class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        for (String word : dic) {
            for (int i = 0; i < spell.length; i++) {
                if (word.contains(spell[i])) {
                    if (i == spell.length - 1) {
                        answer = 1;
                        break;
                    }
                    continue;
                } else {break;}
            }
            if (answer == 1) {break;}
        }
        return answer;
    }
}