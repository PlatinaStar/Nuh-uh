from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Ezekiel's Identity Crisis Shop")

@app.route("/shop")
def shop():
    return render_template("shop.html", title = "EICS Shop")

@app.route("/about")
def about():
    return render_template("about.html", title = "EICS About us")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title = "EICS Contacts")


if __name__ == "__main__":
    app.run()