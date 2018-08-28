import java.util.*;
public class SubstringCompare
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        String small,large,temp;
        String s=sc.next();
        int n=sc.nextInt();
        String sarr[]=new String[200];
        for(int i=n;i<(s.length()+1);i++)
            {
                temp=s.substring(i-n,i);
                sarr[i-n]=temp;
            }
        small=large=sarr[0];
        for(int j=0;j<(s.length()+1-n);j++)
            {
                if(small.compareTo(sarr[j])>0)
                    {
                        small=sarr[j];
                    }
                if(large.compareTo(sarr[j])<0)
                    {
                        large=sarr[j];
                    }
            }
        System.out.println(small);
        System.out.println(large);
    }
}