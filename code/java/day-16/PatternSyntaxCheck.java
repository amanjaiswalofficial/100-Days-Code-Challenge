import java.util.Scanner;
import java.util.regex.*;

public class PatternSyntaxCheck {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String st="";
        int testCases = Integer.parseInt(in.nextLine());
        while (testCases > 0) 
        {
            String pattern = in.nextLine();
            try {
                Pattern r = Pattern.compile(pattern);
                st=st+"Valid\n";
            } catch (Exception e) {
                st=st+"Invalid\n";
            }
            testCases--;
        }
        System.out.println(st);//Printing the final string
        System.out.println("\n");
    }
}