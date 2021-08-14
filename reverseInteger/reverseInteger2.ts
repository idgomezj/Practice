class solution2{
    reverse_integer2(x : number){
        if (!Number.isInteger(x)){
            return " X is different from an integer";
                    } else {
            if ( x < 2**31 -1 && x > -(2**31)){
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



console.log(new solution2().reverse_integer2(131));
console.log(new solution2().reverse_integer2(-123));
console.log(new solution2().reverse_integer2(120));
console.log(new solution2().reverse_integer2(0));