import java.io.*;
import java.util.*;

public class N11 {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String iString; 
        String pString; 

        System.out.print("Enter input string: ");
        iString = input.nextLine();

        System.out.print("Enter pattern string: ");
        pString = input.next();

        input.close();

        System.out.println("Smallest Window:" + getWindow(iString, pString));
    }


    public static String getWindow (String iString, String pString) {

        String result = null;

        if (iString.length() < pString.length()){
            System.out.println("Pattern string is greater than input string;");
            return "";
        }

        int value = 0;
        String[] sArray = new String[iString.length()];

        for (int i = 0; i < iString.length(); i++){
            if (pString.contains(iString.charAt(i) + "") && iString.substring(i).length() >= pString.length()){
                sArray[value++] = iString.substring(i);
            }
        }

        for (int o = 0; o < value; o++){

            String tString = sArray[o];
            char[] cArray = pString.toCharArray();

            int count = cArray.length;
            int lIndex = 0;


            for (int i = 0; i < cArray.length; i++){

                if (tString.contains(cArray[i] + "")){
                    if (lIndex < tString.indexOf(cArray[i])){
                        lIndex = tString.indexOf(cArray[i]);
                    }

                    tString = tString.substring(0, tString.indexOf(cArray[i])) + '\0' + tString.substring(tString.indexOf(cArray[i]) + 1);
                    cArray[i] = '\0';
                    count--;
                }
            }

            if (count <= 0){
                sArray[o] = sArray[o].substring(0, lIndex + 1);
                result = sArray[o].length() < result.length() ? sArray[o] : result;
            }
        }
        return result;
    }
}
