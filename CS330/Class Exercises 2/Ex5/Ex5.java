package Ex5;

import java.util.*;

public class Ex5 {
    public static void main(String[] args) {
        runProgram();
    }

    public static void runProgram() {
        Scanner input = new Scanner(System.in);

        String iString = null;

        System.out.print("Enter Statement (Bowler, Batsman, Fielder, All Rounder, or Audience): ");
        iString = input.nextLine();

        input.close();

        switch (iString) {
        case "bowler":
            System.out.println("Bowler is bowling");
            break;
        case "batsman":
            System.out.println("Batsman is batting");
            break;
        case "fielder":
            System.out.print("Fielder is fielding");
            break;
        case "all rounder":
            System.out.println("Cricketer can bat, bowl & field");
            break;
        case "audience":
            System.out.println("We are interested in caramel popcorn");
            break;
        default:
            System.out.println("Invalid Input");
            break;
        }
    }
}
