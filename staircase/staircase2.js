var staircase2 = /** @class */ (function () {
    function staircase2() {
    }
    staircase2.prototype.solve = function (n) {
        if (n < 0 || n > 100) {
            return;
        }
        var resolve = "";
        resolve = " ".repeat(n - 1) + "#";
        for (var i = n - 2; i >= 0; i--) {
            resolve += "\n" + " ".repeat(i) + "#".repeat(n - i);
        }
        return resolve;
    };
    return staircase2;
}());
var const_class2 = new staircase2();
console.log(const_class2.solve(6));
