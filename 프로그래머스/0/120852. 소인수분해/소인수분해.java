import java.util.ArrayList;
import java.util.HashSet;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int n) {
        HashSet<Integer> primeFactors = new HashSet<>();
        int i = 2;
        while (n != 1) {
            if (n % i == 0) {
                primeFactors.add(i);
                n /= i;
            } else {
                i++;
            }
        }
        return primeFactors.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}