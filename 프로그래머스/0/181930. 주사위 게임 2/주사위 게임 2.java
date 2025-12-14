import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int solution(int a, int b, int c) {
        HashSet<Integer> set = new HashSet<>(Arrays.asList(a, b,c));
        int answer = 0;
        if (set.size() == 3) {
            answer = a + b + c;
        } else if (set.size() == 2) {
            answer = (a + b + c) * (int)(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2));
        } else {
            answer = (a + b + c) * (int)(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2)) * (int)(Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3));
        }
        return answer;
    }
}