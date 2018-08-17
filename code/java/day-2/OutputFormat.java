import java.util.Scanner;

public class OutputFormat
{
    public static void main(String[] args)
    {
        String finals="";
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<3;i++)
        {
            String s=sc.next();
            int j=sc.nextInt();
            for(int k=s.length();k<15;k++)
                {
                    s=s+" ";
                }
            //j=Integer.parseInt(String.format("%03d",j));
            //j='0'+j;
            finals=finals+s+String.format("%03d",j)+'\n';   
        }
        System.out.println("================================");
        System.out.print(finals);
        System.out.println("================================");
    }
}