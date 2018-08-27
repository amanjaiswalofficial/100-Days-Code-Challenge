import java.util.Scanner;

public class JavaSubstring{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        int l1=sc.nextInt();
        int l2=sc.nextInt();
        System.out.println(s.substring(l1,l2));
        }
}