import java.util.*;

public class Ex4 {
    public static void main(String[] args) {


        Scanner textInput = new Scanner(System.in);
        

        System.out.print("Enter number of Rows: ");
        int rows = textInput.nextInt();

        System.out.print("Enter number of Columns: ");
        int columns = textInput.nextInt();

        int[][] a = new int[rows][columns];

        for (int c = 0; c < rows; c++){
            for (int r = 0; r < columns; r++){
                System.out.print("Enter a number: ");
                int num = textInput.nextInt();
                a[c][r] = num;
            }
            System.out.println();
            if (c != rows - 1){
                System.out.println("NEXT COLUMN");
            }
        }

        //Check if row exists
        Comparator<int[]> comparator = new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return Arrays.toString(o1).compareTo(Arrays.toString(o2));
            }
        };

        // Create a set from new values
        Set<int[]> set = new TreeSet<int[]>(comparator);

        // Move every row to the set
        for (int[] row : a){
            set.add(row);
        }

        //Print out the new set
        for (int[] x : set) {
            for (int y : x) {
                System.out.print(y + " ");
            }
            System.out.println();
        }

        textInput.close();
    }
    
}
