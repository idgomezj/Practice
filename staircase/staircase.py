"""
Staircase detail

This is a staircase of size n=4

   #
  ##
 ###
####

Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer, , denoting the size of the staircase.

Constraints

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.


"""


class staircase:
    def solve(self, n: int) -> str:
        if n < 0 or n > 100:
            return
        result = " "*(n-1)+"#"
        for i in range(n-1, 0, -1):
            result += "\n" + " "*(i-1)+"#"*(n-i+1)
        return result


if "__main__" == __name__:
    print(staircase().solve(4))
