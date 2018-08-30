/**
 * StringAnagrams
 */
import java.util.*;
public class StringAnagrams {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s1=sc.nextLine();
        String s2=sc.nextLine();
        char temp;
        int count1=0,count2=0;
        boolean flag=true;
        s1=s1.toLowerCase();
        s2=s2.toLowerCase();
        for(int i=0;i<s1.length();i++)
            {
                temp=s1.charAt(i);
                for(int j=0;j<s1.length();j++)
                    {
                        if(temp==s1.charAt(j))
                            {
                                count1++;
                            }
                        if(temp==s2.charAt(j))
                            {
                                count2++;
                            }
                    }
                if(count1!=count2)
                    {
                        flag=false;
                    }
                count1=0;
                count2=0;
            }
    if(flag)
        {
            System.out.println("Anagrams");
        }
    else{
        System.out.println("Not Anagrams");
        }
    }
}