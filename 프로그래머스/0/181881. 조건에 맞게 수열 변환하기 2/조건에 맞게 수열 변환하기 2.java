import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int[] before = new int[arr.length];
        while (true) {
            for (int i = 0; i < arr.length; i++) {
                before[i] = arr[i];
            }
            for (int i = 0; i < arr.length; i++) {
                int n = arr[i];
                if (n >= 50 && n % 2 == 0) {
                    arr[i] = n / 2;
                } else if (n < 50 && n % 2 == 1) {
                    arr[i] = n * 2 + 1;
                } else {
                    arr[i] = n;
                }
            }
            if (Arrays.equals(arr, before)) {
                break;
            }
            answer++;
        }
        return answer;
    }
}