import java.util.*;
import java.io.*;
public class Datatypes
{
    public static void main(String[] args)
    {
        long a[]=new long[100];
        int x,j;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        try {
            
            for (j = 0; j < x; j++) {
                long temp;
                temp = sc.nextLong();
                a[j] = temp;
            }
            for (j = 0; j < x; j++) {

                System.out.println(a[j] + " can be fitted in ");
                if (a[j] >= -32768 && a[j] <= 32767) {
                    System.out.println("*short");
                }
                if (a[j] >= (Math.pow(-2, 31)) && a[j] <= (Math.pow(2, 31) - 1)) {
                    System.out.println("*int");
                }
                if (a[j] >= (Math.pow(-2, 63)) && a[j] <= (Math.pow(2, 63) - 1)) {
                    System.out.println("*long");
                }

            }
        } catch(Exception e)
                {
                    System.out.println(sc.next()+" can't be fit anywhere");
                }
        
        }
}