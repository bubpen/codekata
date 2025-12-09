import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder new_a = new StringBuilder(a.length());
        for (char c : a.toCharArray()) {
            if (Character.isUpperCase(c)) {
                new_a.append(Character.toLowerCase(c));
            } else {
                new_a.append(Character.toUpperCase(c));
            }
        }
        System.out.println(new_a);
    }
}