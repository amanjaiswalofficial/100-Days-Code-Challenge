/**
 * StringTokens
 */
import java.util.*;
public class StringTokens {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String sarr[]=new String[100];
        //=new Char[10];
        String sct="!,?._@'";
        for(int i=0;i<s.length();i++)
            {
                /*if(s.charAt(i)==' ')
                    {
                      
                    }*/
            }
        sarr=s.split(sct);
        //f1=sarr.split(carr[0]);
        //f2=sarr.split(carr[1]);
        //f3=sarr.split(carr[2]);
        for(int j=0;j<sarr.length;j++)
            {
                System.out.println(sarr[j]);
            }
    }

}
