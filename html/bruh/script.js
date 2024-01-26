function Time() {
  const d = new Date();
  document.getElementById("time").innerHTML = "<br>" + d;
}

function Name() {
  let text;
  let person = prompt("Gib name:", "");
  if (person == null || person == "") {
    text = "Tell me your name, mortal.";
  } else {
    text = `So you are <span style="color: green;">${person}</span>, huh.`;
  }
  document.getElementById("name").innerHTML = text;
}

let x = '1';
function chang(){
  switch (x) {
    case '1':
     document.getElementById("change").innerHTML = `<p style="color: orange;">I'm orindž <p/>`;
      x = '0';
      break;
    case '0':
      document.getElementById("change").innerHTML = `<p style="color: green;">I'm grín<p/>`;
      x = '1';
      break;
  }
}

y = 1;
function secret() {
  if (y) {
    document.getElementById("secrete").innerHTML = 'This... I have this';
    document.getElementById("img").innerHTML = `<img src="secret.jpg" height="500vw" alt="Can't see it? What a shame." title="img by Tv_Head_Static">`;
    y = 0;
  }
  else {
    document.getElementById("img").innerHTML = `And it's gone`;
    document.getElementById("secrete").remove();
  }
}