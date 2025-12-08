class Solution {
    public int solution(int a, int b) {
        int answer = 1;
        if (a == b || a % b == 0) {
            answer = 1;
            return answer;
        }
        int m = Math.min(a, b);
        int M = Math.max(a, b);
        int gcd = 1;
        for (int i = m; i > 0; i--) {
            if (m % i == 0) {
                if (M % i == 0) {
                    gcd = i;
                    break;
                }
            }
        }
        b /= gcd;
        int d = 2;
        if (b == 2 || b == 5) {
            answer = 1;
        } else {
            while (b > 1 && d <= b) {
                if (b % d == 0) {
                    if (d != 2 && d != 5) {
                        answer = 2;
                        break;
                    } else {
                        b = b / d;
                    }
                } else {
                    d++;
                }
            }
        }
        return answer;
    }
}