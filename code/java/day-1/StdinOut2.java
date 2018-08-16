import java.util.Scanner;

public class StdinOut2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double j=scan.nextDouble();
        scan.nextLine();
        String s=scan.nextLine();
        

        System.out.println("String: " + s);
        System.out.println("Double: " + j);
        System.out.println("Int: " + i);
    }
}