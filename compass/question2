import java.util.Scanner;

public class Application2 {
    public static void main (String []args) {
        Scanner source = new Scanner(System.in);
        String line = source.nextLine();
        String[] elements = line.split(" ");
        int upsetCount = 0, funCount = 0;

        for (String word : elements) {
            if (word.equals(":-(")){
                upsetCount++ ;
            } else if (word.equals(":-)")){
                funCount++;
            }
        }
        if (upsetCount==funCount){
            System.out.println("Neutral");
        } else if (upsetCount > funCount) {
            System.out.println("Upset");
        } else {
            System.out.println("Fun");
        }

    }
}
