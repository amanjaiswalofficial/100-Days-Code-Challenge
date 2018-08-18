import java.util.*;
public class Loops
{
    public static void main(String[] args)
    {
        int a;
        Scanner sc=new Scanner(System.in);
        a=sc.nextInt();
        for(int i=1;i<11;i++)
            {
                System.out.format("%d x %d = %d\n",a,i,a*i);
            }
    }
}