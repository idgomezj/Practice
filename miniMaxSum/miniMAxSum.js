class miniMaxSum {

    solve( arr){
        for(let x of arr){
            if(x<1 || x>Math.pow(10,9) ){
                return "";
            }
                }
        arr = arr.sort();
        return arr.slice(0,4).reduce(this.add,0) + " " + 
        arr.slice(arr.lenght-4,arr.length).reduce(this.add,0);
        
    }

    add(accumulator,a){
        return accumulator + a;
    }

    

}


const miniMaxSum_class= new miniMaxSum();
console.log(miniMaxSum_class.solve([1,2,3,4,5]))