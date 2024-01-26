const HIGHEST = Number.MAX_SAFE_INTEGER;

function Inputha(valuee) {
  valuee = parseFloat(valuee)
  if (isNaN(valuee) == false && valuee != 1 && valuee != 2) {
    document.getElementById("puf").innerHTML = "□";
  }
  else if (valuee == 2) { document.getElementById("puf").innerHTML = "2" }
  else {document.getElementById("puf").innerHTML = "1"}
}

function Calculate(sign) {
  var one = parseFloat(document.getElementById("first").value);
  var two = parseFloat(document.getElementById("second").value);
  var num = [0, 0];
  var click = false
  var ans;
  var ans2;
  num[0] = one;
  num[1] = two;

  if (sign == "^" && Number.isNaN(num[1]) || sign == "^" && click == true) { num[1] = 1; two = 1; click = true; }; //makes sure exponent is 1 if there's no second input

  if (sign == "√" && Number.isNaN(num[1]) || sign == "√" && click == true) { num[1] = 2; two = 2; click = true; }; //makes sure the root is square if there's no second input

  if (Number.isNaN(one) || Number.isNaN(two)) { //makes sure none of the numbers are NaN
    alert("Error");
    return;
  }

  if (one > HIGHEST || two > HIGHEST) { //makes sure the user doesn't go beyond the limit
    alert(`You cannot go beyond ${HIGHEST}`);
    return;
  }
  switch (sign) {
    case "+": //add
      ans = num[0] + num[1];
      break;
    case "-": //subtract
      ans = num[0] - num[1];
      break;
    case "*": //multiply
      ans = num[0] * num[1];
      break;
    case "/": //divide 
      ans = num[0] / num[1];
      ans2 = num[0] % num[1];
      ans = ans + ' (reminder: ' + ans2 + ')';
      break;
    case "%": //percentage
      ans = (100 * num[1]) / num[0] + "%";
      break;
    case "^": //exponentiation
      if (Number.isNaN(num[1])) num[1] = 1;
      ans = Math.pow(num[0], num[1]);
      break;
    case "√": //root
      if (Number.isNaN(num[1])) num[1] = 2;
      ans = Math.pow(num[0], 1 / num[1]);
      break;
  }
  if (Number.isNaN(ans)) { //Shows when the math doesn't make sense
    alert("nuh uh");
    return;
  }
  document.getElementById("answer").innerHTML = ans;
}

let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'the day your first born will be born'];
let pronouns = ['you', 'I', 'he', 'she', 'they'];
let actions = ['kill', 'hide', 'fart on', 'dance on', 'microwave', 'snap', 'scare', 'put', 'steam', 'bake', 'hug', 'smell'];
let recievers = ['a dog', 'your best friend', 'a cake', 'a pie', 'your grandma', 'Rex Lapis', 'a keyboard'];
function RWG() {
  let day = days[Math.floor(Math.random() * days.length)];
  let pron = pronouns[Math.floor(Math.random() * pronouns.length)];
  let action = actions[Math.floor(Math.random() * actions.length)];
  let reciever = recievers[Math.floor(Math.random() * recievers.length)];
  if (action == 'put') {
    document.getElementById("sentenence").innerHTML = `On ${day} ${pron} will ${action} ${reciever} in my mouth.`;
  }
  else document.getElementById("sentenence").innerHTML = `On ${day} ${pron} will ${action} ${reciever}.`;
}

const x = Math.PI;

function haiya() {
  let r = parseFloat(document.getElementById("txt").value);
  const r2 = r * r;
  let fufu = [4 * x * r2];
  document.getElementById("ansr").innerHTML = `${fufu}`;
}

let n = 25;

const sqrt = Math.sqrt(n);

function sqerut() {
  document.getElementById("hahaha").innerHTML = `Square root of ${n} is ${sqrt}`;
}

function haiyaa() {
  let u = parseFloat(document.getElementById("txtt").value);
  let s = parseFloat(document.getElementById("txttt").value);
  const u2 = u * u;
  let fuf = [x * u2 + x * u * s];
  document.getElementById("ansrr").innerHTML = `${fuf}`;
}

var aver = document.getElementById("avrg")
var o = []
var y = 0
let averag = 0

function Average(input){
  o.push(parseFloat(input))
  console.log(o)
  let top = 0
  for (let i = 0; i < o.length; i++){
    top += o[i]
  }
  averag = top/(o.length)
}

function gib(){
  document.getElementById("yourAverage").innerHTML = averag
}
