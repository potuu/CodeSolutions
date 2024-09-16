/*
The challenge here is to read nn lines of input until you reach EOF, then number and print all nn lines of content.

Hint: Java's Scanner.hasNext() method is helpful for this problem.

Input Format
Read some unknown nn lines of input from stdin(System.in) until you reach EOF; each line of input contains a non-empty String.

Output Format
For each line, print the line number, followed by a single space, and then the line content received as input:

k This is the line read as input for line number 'k'.
Sample Input

Hello world
I am a file
Read me until end-of-file.
Sample Output

1 Hello world
2 I am a file
3 Read me until end-of-file.
*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input=new Scanner(System.in);
        String line;
        int i=1;
        while(input.hasNext()){
            line=input.nextLine();
            System.out.println(i+" "+line);
            i++;
        }
    }
}
