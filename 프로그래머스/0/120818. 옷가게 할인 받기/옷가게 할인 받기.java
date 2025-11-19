class Solution {
    public int solution(int price) {
        int answer = price;
        if ( price >= 100000) {
            answer = (int)(0.95 * price);
        }
        if (price >= 300000) {
            answer = (int)(0.9 * price);
        }
        if (price >= 500000) {
            answer = (int)(0.8 * price);
        }
        return answer;
    }
}