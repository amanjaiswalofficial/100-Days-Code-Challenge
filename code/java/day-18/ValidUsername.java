import java.util.Scanner;

/**
 * ValidUsername
 */
public class ValidUsername {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String finals="";
        int n=sc.nextInt();
        sc.nextLine();
        for(int i=0;i<n;i++)
            {
                String s=sc.next();
                //System.out.println(s);
                if(s.length()>=8 && s.length()<=30)
                    {
                        
                        if(!(String.valueOf(s.charAt(0)).matches("[A-Z]||[a-z]")))//checking if first letter is alphabet or not
                            {
                                finals=finals+"Invalid\n";
                                continue;
                            }
                        else{
                            boolean flag=true;
                            for (int j = 0; j < s.length(); j++) {

                                if(!(String.valueOf(s.charAt(j)).matches("[A-Z]||[a-z]||[0-9]||_")))//checking if all others are alphanumeric or _ or not
                                    {
                                        flag=false;
                                    }
                                
                            }
                            if (flag) {
                        finals = finals + "Valid\n";

                    } else {
                        finals = finals + "Invalid\n";
                    }
                        }
                    }
                else{
                    finals=finals+"Invalid";

                }
                
            }
            System.out.println(finals);
    }
}