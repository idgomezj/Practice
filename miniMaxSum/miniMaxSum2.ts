class miniMaxSum2{
    solve(arr: any): string{
        for (let x of arr){
            if(x< 1 || x >Math.pow(10,9)){
                return "";
            }
        }
        arr=arr.sort();
        return arr.slice(0,4).reduce(this.add,0) + " " + arr.slice(arr.lenght -4,arr.lenght).reduce(this.add,0)

    }

    add(accumulation: number,a:number): number{
        return accumulation+a;
    }
}

const miniMaxSum_class2= new miniMaxSum2();
console.log(miniMaxSum_class2.solve([1,2,3,4,5]))