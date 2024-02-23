from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Web Theory")

if __name__ == "__main__":
    app.run()