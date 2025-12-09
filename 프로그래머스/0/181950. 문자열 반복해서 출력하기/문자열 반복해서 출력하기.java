import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            if (i == n-1) {
                System.out.println(str);
            } else {
                System.out.print(str);
            }
        }
    }
}