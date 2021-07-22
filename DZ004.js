//задание1
let size = prompt('Введите размер вклада');
let percent = prompt('Введите ставку в процентах');
let month = prompt('Введите количество месяцев');


function CompoundInterest(size, percent, month, sum = size){
    if (month <= 0){
        return sum;
    }
  	console.log(sum);
    return CompoundInterest(size, percent, month-1,sum+parseFloat(sum)*parseFloat(percent)/100/12)
}
console.log(CompoundInterest(parseFloat(size), parseFloat(percent), parseFloat(month)).toFixed(3));
//задание2
for (let y = 1; y < 3; y = y + 1){
    for (let x = 1; x < 3; x = x + 1){
        drawRect(x*70, 0, 10,220, 'black')
    }
    drawRect(0, y*70, 220,10, 'black')
}

function TicTacToe(left,top,size){
drawRect(left, top, size, size, 'black');
    for (let y = 0; y < 3; y = y + 1) {
        for (let x = 0; x < 3; x = x + 1) {
            drawRect((x * 50)+left, (y * 50)+top, 45, 45, 'white');
        }
    }
}
console.log(TicTacToe(100,100,140))

function TicTacToe(left,top,step){
    for (let y = 0; y < 3; y = y + 1) {
        for (let x = 0; x < 3; x = x + 1) {
            drawRect(x*step, 0, 1,step*3, 'black')
        }
        drawRect(0, y*step, step*3,1, 'black')
    }
}
console.log(TicTacToe(100,100))

function TicTacToe(left,top,step,color){
    for (let y = 1; y < 3; y = y + 1) {
        for (let x = 1; x < 3; x = x + 1) {
            drawRect(left+x*step, top, 1,step*3, color)
        }
        drawRect(left, top+y*step, step*3,1, color)
    }
}
console.log(TicTacToe(190,190,30,'red'));
console.log(TicTacToe(145,145,60,'green'));
console.log(TicTacToe(100,100,90,'blue'));