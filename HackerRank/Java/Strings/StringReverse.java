/*
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

Given a string A, print Yes if it is a palindrome, print No otherwise.

Constraints

A will consist at most 50 lower case english letters.
Sample Input

madam
Sample Output

Yes
*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        String rev = "";
        for( int i=A.length()-1; i>=0; i--) {
        rev += A.charAt(i);
        } if(A.compareTo(rev)==0) {
        System.out.print("Yes");
        } else {
        System.out.print("No");
        }     
        
    }
}



