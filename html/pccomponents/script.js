
function Popup(elem) {
  var name = elem.textContent;
  if (confirm("You're about to travel to another page.")) {
    alert("Alright then, here we go!");
    switch (name) {
      case "Home":
        window.location.href = "index.html";
        break;

      case "Contacts":
        window.location.href = "contacts.html";
        break;

      case "Store":
        window.location.href = "store.html";
        break;

      case "About":
        window.location.href = "about.html";
        break;
    }
  }
  else {
    alert("Take your time.");
  }
}

function Popup2() {
  alert("Yeah uhhh... You kinda already are here");
  document.getElementById("removal").remove();
}

function Colour() {
  document.write("<h2 style='color:#" + Math.floor(Math.random() * 16777216).toString(16) + "; font-size: 40px;'>");
}

function Cart(product, price, el) {

  localStorage.setItem(product, price);
  products += 1;
  document.getElementById("amount").innerHTML = `&nbsp${products}&nbsp`;
  alert(`${product} was added to the cart!`);
}

let products = localStorage.length;

document.getElementById("amount").innerHTML = `&nbsp${products}&nbsp`;

