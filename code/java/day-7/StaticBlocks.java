import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

//Understanding about static blocks
public class StaticBlocks {

    
static int B=0,H=0;
static boolean flag;
static
{
    Scanner sc=new Scanner(System.in);
    B=sc.nextInt();
    H=sc.nextInt();
    if(B>0 && H>0)
    {
        flag=true;
    }
    else
    {
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}//this block doesnt need to be initialized it is called automatically

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

