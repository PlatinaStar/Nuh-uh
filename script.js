x = 1
y = false
if (screen.orientation.type == 'landscape-primary' || screen.orientation.type == 'landscape-secondary'){
    for (i = 0 ; i < document.getElementById("gridder").children.length ; i++) {
        document.getElementById("gridder").children[i].classList += "ROWWWS"
        x++
        if (x == document.querySelectorAll('#gridder .gridderitem').length + 2 && y != true) {
            x = 1
            y = true
        }
    }
}
else {
    for (i = 0 ; i < document.getElementById("gridder").children.length ; i++) {
        document.getElementById("gridder").children[i].style = ""
        y = false
    }
    x = 1
}
screen.orientation.onchange = function (){
    if (screen.orientation.type == 'landscape-primary' || screen.orientation.type == 'landscape-secondary'){
        for (i = 0 ; i < document.getElementById("gridder").children.length ; i++) {
            document.getElementById("gridder").children[i].style = "grid-row: " + x + ";"
            x++
            if (x == document.querySelectorAll('#gridder .gridderitem').length + 2 && y != true) {
                x = 1
                y = true
            }
        }
    }
    else {
        for (i = 0 ; i < document.getElementById("gridder").children.length ; i++) {
            document.getElementById("gridder").children[i].style = ""
            y = false
        }
        x = 0
    }
}