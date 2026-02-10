class Solution {
    public String[] solution(String[] names) {
        int group = names.length % 5 == 0? names.length / 5 : names.length / 5 + 1;
        String[] answer = new String[group];
        for (int i = 0; i < names.length; i += 5) {
            answer[i / 5] = names[i];
        }
        return answer;
    }
}