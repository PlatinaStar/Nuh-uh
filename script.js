x = 1
for (i = 0 ; i < 18 ; i++) {
    document.getElementById("gridder").children[i].style = "grid-row: " + x + ";"
    x++
    if (x == 10) {
        x = 1
    }
}