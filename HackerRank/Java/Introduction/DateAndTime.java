/*
The Calendar class is an abstract class that provides methods for converting between a specific instant in time and a set of calendar fields such as YEAR, MONTH, DAY_OF_MONTH, HOUR, and so on, and for manipulating the calendar fields, such as getting the date of the next week.

You are given a date. You just need to write the method, getDay, which returns the day on that date. To simplify your task, we have provided a portion of the code in the editor.

Example
month=8
day=14
year=2017

The method should return MONDAY as the day on that date.

**image**

Function Description
Complete the findDay function in the editor below.

findDay has the following parameters:

int: month
int: day
int: year

Returns
string: the day of the week in capital letters

Input Format
A single line of input containing the space separated month, day and year, respectively, in MM/DD/YYYY format.

Constraints
2000<year<3000

Sample Input
08 05 2015

Sample Output
WEDNESDAY

Explanation
The day on August 5th 2015 was WEDNESDAY.
*/


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

public static String findDay(int month, int day, int year) {
     Calendar calendar = Calendar.getInstance();

    // Set the calendar with the provided date (Note: month is 0-based in Calendar)
    calendar.set(year, month - 1, day);

    // Get the day of the week (1 = Sunday, 2 = Monday, ..., 7 = Saturday)
    int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);

    // Array to map the day of the week to its name
    String[] days = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};

    // Return the corresponding day name
    return days[dayOfWeek - 1];

}
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
