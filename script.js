x = 1
y = false
for (i = 0 ; i < document.getElementById("gridder").children.length ; i++) {
    document.getElementById("gridder").children[i].style = "grid-row: " + x + ";"
    x++
    if (x == document.querySelectorAll('#gridder .gridderitem').length + 2 && y != true) {
        x = 1
        y = true
    }
}