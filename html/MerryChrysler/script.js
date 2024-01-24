var y = 0;
requestAnimationFrame(move);
var body = document.body;
function move(){
    y += 0.25;
    body.style.backgroundPosition = '0px ' + y + 'px';
    requestAnimationFrame(move);
}

function Rando() {
  
}