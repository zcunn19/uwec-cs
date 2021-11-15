package Ex1;

import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        getGrade();
    }

    public static void getGrade() {
        String name = "Chase";
        int gradeNum;
        int score;

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a grade: ");
        gradeNum = input.nextInt();

        System.out.print("Enter a score: ");
        score = input.nextInt();

        String sGrade = null;
        String sScore = null;

        switch (gradeNum) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            sGrade = "Elementary";
            break;
        case 6:
        case 7:
        case 8:
            sGrade = "Middle";
            break;
        case 9:
        case 10:
        case 11:
        case 12:
            sGrade = "High";
            break;
        }

        switch (score / 10) {
        case 10:
        case 9:
        case 8:
            sScore = "Excellent";
            break;
        case 7:
        case 6:
            sScore = "Distinction";
            break;
        case 5:
        case 4: 
            sScore = "Poor";
            break;
        default:
            sScore = "Invalid Input";
            break;
        }

        System.out.println("Chase is in " + sGrade + " School in grade " + gradeNum + ".");
        System.out.println("He got a " + sScore + " score.");
    }
}
