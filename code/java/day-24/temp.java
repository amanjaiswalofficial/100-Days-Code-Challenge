import java.util.*;
class temp
{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String x=sc.next();
        int count=0;
        String temps="";
        String chars="";
        int maxcount=0;
        for (int i = 0; i < x.length(); i++) {
            temps=String.valueOf(x.charAt(i));
            count=0;
        
            for(int j=0;j<x.length();j++)
                {
                    char c=temps.charAt(0);
                    if(c==x.charAt(j))
                        {   
                            count++;
                            
                        }
                }
            if(count>=maxcount)
                {
                    maxcount=count;
                    chars=temps;
                }
        }
    System.out.println(chars);
    }
}