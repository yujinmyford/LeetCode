class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
        int len1 = str1.length();
        int len2 = str2.length();
        
        int gcd = len1 > len2 ? computeGCD(len1,len2) : computeGCD(len2,len1);
        
        String res = len1 < len2 ? str1.substring(0, gcd) : str2.substring(0, gcd);
        
        String str1Generated = generateString(res, len1/gcd);
        String str2Generated = generateString(res, len2/gcd);
        
        if(str1.equals(str1Generated) && str2.equals(str2Generated)) return res;
        return "";
    }
    
    private int computeGCD(int len1, int len2) {
        if(len2 == 0) return len1;
        return computeGCD(len2, len1 % len2);
    }
    
    private String generateString(String str, int times) {
        String res = "";
        for(int i = 0; i < times; i++) {
            res += str;
        }
        return res;
    }
}