class Solution {
    public int solution(int hp) {
        int answer = 0;
        int i = 0;
        int j = 0;
        int k = 0;
        while (hp > 0) {
            if (hp >= 5) {
                i = hp/5;
                hp -= 5 * i;
            } else if (hp >= 3) {
                j = hp / 3;
                hp -= 3 * j;
            } else {
                k = hp;
                hp = 0;
            }
        }
        answer = i + j + k;
        return answer;
    }
}