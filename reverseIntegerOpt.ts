/*
Given a signed 32-bit integer x, return x 
with its digits reversed. If reversing x causes the value to 
go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
*/

function reverse_integer2(x:number):  number {
    const limit = 2**31;
    const k = x < 0 ? -1 : 1;
    const n= Number(String(Math.abs(x)).split('').reverse().join(''));
    return n > limit ? 0 : n * k;
}


/*
Example 1:
    Input: x = 123
    Output: 321
Example 2:
    Input: x = -123
    Output: -321
Example 3:
    Input: x = 120
    Output: 21

Example 4:
    Input: x = 0
    Output: 0

    */


    console.log(reverse_integer2(131));
    console.log(reverse_integer2(-123));
    console.log(reverse_integer2(120));
    console.log(reverse_integer2(0));