import java.util.Scanner;
public class Regex {

      public static void main(String[] args) {
          Scanner sc=new Scanner(System.in);
          int n=sc.nextInt();//No. of inputs to check for
          String finals="";
          sc.nextLine();//to skip a newline
          for(int i=0;i<n;i++)
            {
                String s = sc.nextLine();
                String arr[]=s.split("\\.");//perform splitting of inpute
                if(arr.length==4)//condition check
                    {
                        if((Integer.parseInt(arr[0])>=0 && Integer.parseInt(arr[0])<=255) && 
                            (Integer.parseInt(arr[1]) >=0 && Integer.parseInt(arr[1]) <=255) &&
                              (Integer.parseInt(arr[2]) >=0 && Integer.parseInt(arr[2]) <=255) &&
                               (Integer.parseInt(arr[3])>=0 && Integer.parseInt(arr[3])<=255))
                            {
                                finals = finals + "true\n";
                            }
                            else{
                                finals=finals+"false\n";
                            }                       
                    }
                else{
                        finals=finals+"false\n";
                }
            }
        System.out.println(finals);//print final output whether true or false.
          
      }
}
