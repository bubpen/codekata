import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int center = array.length / 2;
        int answer = array[center];
        return answer;
    }
}