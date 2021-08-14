/*
Given a signed 32-bit integer x, return x 
with its digits reversed. If reversing x causes the value to 
go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
*/

class solution {
    reverse_integer(x){
        if (!Number.isInteger(x)){
return " X is different from an integer";
        } else {
if ( x < 2^31 -1 && x > -2^31){
if (x<0){

return Number(String(Math.abs(x)).split('').reverse().join('')) * -1;
} else {
    return Number(String(x).split('').reverse().join(''));
}
} else {
    return 0
}
        }
    }
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


console.log(new solution().reverse_integer(131));
console.log(new solution().reverse_integer(-123));
console.log(new solution().reverse_integer(120));
console.log(new solution().reverse_integer(0));