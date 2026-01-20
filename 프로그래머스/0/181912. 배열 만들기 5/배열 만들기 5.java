import java.util.ArrayList;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (String str : intStrs) {
            str = str.substring(s, s + l);
            if (Integer.parseInt(str) > k) {
                answer.add(Integer.parseInt(str));
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}