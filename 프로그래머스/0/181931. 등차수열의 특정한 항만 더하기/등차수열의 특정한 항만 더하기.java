class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int sum = a;
        for (int idx = 0; idx < included.length; idx++) {
            if (idx > 0)  {sum += d;}
            if (included[idx] == true) {answer += sum;}
        }
        return answer;
    }
}