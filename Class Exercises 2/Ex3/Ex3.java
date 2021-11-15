package Ex3;

import java.util.*;

public class Ex3 {
    public static void main(String[] args) {
        runProgram();
    }

    public static void runProgram() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number 1-15: ");
        int num = input.nextInt();
        int level = 0;

        input.close();
        
        switch (num) {

        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            level = 1;
            break;
        case 6:
        case 7:
        case 8:
        case 9:
        case 10:
            level = 2;
            break;
        case 11:
        case 12:
        case 13:
        case 14:
        case 15:
            level = 3;
            break;
        default:
            System.out.println("Invalid Input");
            break;
        }

        int factorial = 1;

        for (int i = 1; i <= num; i++) {
            factorial = factorial * i;
        }

        System.out.println("The number is from level: " + level);
        System.out.println("The factorial of the number is: " + factorial);
    }
}
