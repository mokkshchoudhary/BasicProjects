//counter program

const decrease = document.getElementById("decrease");
const reset = document.getElementById("reset");
const increase = document.getElementById("increase");
const CountLabel = document.getElementById("CountLabel");
let count = 0;

increase.onclick = function(){
    count++;
    CountLabel.textContent = count;
}

decrease.onclick = function(){
    count--;
    CountLabel.textContent = count;
}

reset.onclick = function(){
    count = 0;
    CountLabel.textContent = count;
}
