class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};
        int x = board[0] / 2;
        int y = board[1] / 2;
        for (String direction : keyinput) {
            if (direction.equals("up")) {
                if (answer[1] < y) {answer[1]++;}
            } else if (direction.equals("down")) {
                if (answer[1] > -y) {answer[1]--;}
            } else if (direction.equals("left")) {
                if (answer[0] > -x) {answer[0]--;}
            } else {if (answer[0] < x) {answer[0]++;}}
        }
        return answer;
    }
}