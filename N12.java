public class N12 {

    public static void main(String[] args) {
   
     String str = "niharika";
     String findStr = "ir";
     String result = "";
   
     if (str.length() < findStr.length()) {
      System.out.println("Pattern string is greater than source string");
      return;
     }
   
     int j = 0;
     String[] arr = new String[str.length()];
     // Get all substring which starts with any one character from the
     // pattern string
     for (int i = 0; i < str.length(); i++) {
      if (findStr.contains(str.charAt(i) + "") && str.substring(i).length() >= findStr.length()) {
       arr[j++] = str.substring(i);
      }
     }
   
     // Iterate all substrings which we generated
     for (int pnt = 0; pnt < j; pnt++) {
   
      String string = arr[pnt];
      char[] tmp = findStr.toCharArray();
   
      int cnt = tmp.length;
      int lastIndex = 0;
   
      // Compare each character from the pattern string with the substring
      // and check for all characters present or not
      for (int i = 0; i < tmp.length; i++) {
   
       if (string.contains(tmp[i] + "")) {
        if (lastIndex < string.indexOf(tmp[i])) {
         lastIndex = string.indexOf(tmp[i]);
        }
        string = string.substring(0, string.indexOf(tmp[i])) + '\0'
          + string.substring(string.indexOf(tmp[i]) + 1);
        tmp[i] = '\0';
        cnt--;
       }
      }
   
      // If all characters present in substring then trim extra characters
      // and choose the smallest window string
      if (cnt <= 0) {
       arr[pnt] = arr[pnt].substring(0, lastIndex + 1);

        // if (result.length() > 0 && arr[pnt].length() < result.length()){
        //     result = arr[pnt];
        // } else {
        //     result = result;
        // }

       result = arr[pnt].length() < result.length() ? arr[pnt] : result;
      }
   
     }
     System.out.println("\nInput String           : " + str);
     System.out.println("\n2nd String to find     : " + findStr);
     System.out.println("\nSmallest window string : " + result);
    }
   }