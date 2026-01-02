import java.util.Arrays;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        int n = db.length;
        for (String[] row : db) {
            if (Arrays.equals(row, id_pw)) {
                return "login";
            }
        }
        String id = id_pw[0];
        String pw = id_pw[1];
        String[] ids = new String[n];
        String[] pws = new String[n];
        for (int i = 0; i < n; i++) {
            ids[i] = db[i][0];
            pws[i] = db[i][1];
        }
        for (int i = 0; i < n; i++) {
            if (ids[i].equals(id)) {
                return "wrong pw";
            }
        }
        return "fail";
    }
}