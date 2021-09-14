class staircase2 {
    solve(n: number){
        if (n<0 || n>100){
            return;
        }
        let resolve="";
        resolve=" ".repeat(n-1)+"#";
        for ( let i=n-2;i>=0;i--){
            resolve +="\n" + " ".repeat(i) + "#".repeat(n-i)
        }
        return resolve
    }
}

let const_class2= new staircase2();
console.log(const_class2.solve(6))