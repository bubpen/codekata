import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList();
        int i = 0;
        while (i < arr.length)  {
            int idx = stk.size() - 1;
            if (stk.isEmpty()) {
                stk.add(arr[i]);
                i++;
            }
            else if (stk.get(idx) < arr[i]) {
                stk.add(arr[i]);
                i++;
            } else {
                stk.remove(idx);
            }
        }
        return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}