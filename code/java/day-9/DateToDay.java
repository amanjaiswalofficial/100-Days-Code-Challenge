import java.text.SimpleDateFormat;
import java.util.*;
import java.text.*;

public class DateToDay
{
    
    public static void main(String[] args)
    {
        Date dt=new Date();
        //String input_date = "01 08 2012";
        String input_date;
        Scanner sc=new Scanner(System.in);
        input_date=sc.nextLine();
        SimpleDateFormat format1 = new SimpleDateFormat("dd mm yyyy");
        
        String dt1 = "25 08 2018"; // Start date
        SimpleDateFormat sdf = new SimpleDateFormat("dd mm yyyy");
        Calendar c = Calendar.getInstance();

        try {
            dt = format1.parse(input_date);

            c.setTime(sdf.parse(dt1));

        } catch (Exception e) {
            System.out.println(e);
        }
        DateFormat format2 = new SimpleDateFormat("EEEE");
        String finals=format2.format(dt);
        System.out.println(finals);


        c.add(Calendar.DATE, 1); // number of days to add
        dt1 = sdf.format(c.getTime());
        System.out.println(dt1);
        }
}