import java.util.*;
public class StringReverse
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String rev="";
        for(int j=s.length()-1;j>=0;j--)
            {
                rev=rev+s.charAt(j);
            }
        if(s.compareTo(rev)==0)
            {
                System.out.println("Yes");
            }
            else{
                System.out.println("No");
            }
    }
}