class staircase {
    constructor(n){
        this.n=n;
    }
    solve(){
        if (this.n<0 ^ this.n>100){
            return;
        };
        let resolve ="";
        resolve=" ".repeat(this.n-1)+"#";
        for (let i=this.n-2;i>=0;i--){
            resolve +="\n" + " ".repeat(i) + "#".repeat(this.n-i)
        };
       return resolve
    }
}

const const_class= new staircase(6)
console.log(const_class.solve())