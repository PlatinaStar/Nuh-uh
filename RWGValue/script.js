let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
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
    let fufu = [4 * x * (r * r)];
    document.getElementById("ansr").innerHTML = `${fufu}`
}
