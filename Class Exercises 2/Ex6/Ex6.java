package Ex6;

import java.util.*;

public class Ex6 {

    static String hasTwoFactors(int A[], int arr_size, int sum) {
        int l, r;

        Arrays.sort(A);

        l = 0;
        r = arr_size - 1;

        while (l < r) {
            if (A[l] + A[r] == sum) {
                return A[l] + " " + A[r];
            } else if (A[l] + A[r] < sum) {
                l++;
            }
            else {
                r--;
            }
        }
        return "";
    }

    public static void main(String args[]) {
        int A[] = new int[255];

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        int arraySize = input.nextInt();

        System.out.println("Enter array values one by one: ");
        for(int i=0; i < arraySize; i++) {
            A[i] = input.nextInt();
         }

         System.out.print("Enter sum to find: ");
         int n = input.nextInt();

         input.close();

         int arr_size = A.length;

         System.out.println("Two factors: " + hasTwoFactors(A, arr_size, n));

    }

}