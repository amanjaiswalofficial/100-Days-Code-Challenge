import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class EOF {

    public static void main(String[] args) {
        String st = "";
        int i = 0;
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            i++;
            String s = sc.nextLine();
            st = st + i + " " + s + "\n";
        }
        System.out.println(st);
    }
}