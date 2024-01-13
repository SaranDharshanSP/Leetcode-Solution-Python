class Solution {
  public int strStr(String haystack, String needle) {
            int a=haystack.length();
            int b=needle.length(); 
            if (a<b) return -1;
            if (b==0) return 0;
            for (int i = 0; i <=a-b; i++) {
                if (haystack.substring(i,i+b).equals(needle)) return i;
            }
        return -1;
        }
}