import java.util.Scanner;

public class Loops2
{
    public static void main(String[] args)
    {
        int x,low,num,high;
        String finals="";
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        for(int j=0;j<x;j++)
            {
                low=sc.nextInt();
                num=sc.nextInt();
                high=sc.nextInt();
                for(int k=0;k<high;k++)
                    {
                      int temp=(int)(Math.pow(2,k));
                      low=low+num*temp;
                      finals=finals+low+" ";
                    }
            finals=finals+"\n";
            }
        System.out.print(finals);
    }
}