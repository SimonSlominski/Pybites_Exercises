from flask import Flask, render_template
from data import f1_teams

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           f1_teams=f1_teams)

if __name__ == "__main__":
    app.run()
