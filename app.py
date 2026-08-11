from flask import Flask, render_template

app = Flask(__name__)

BILLETS = [5, 10, 20, 50, 100, 200, 500]
PIECES = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]

@app.route("/")
def index():
    # return "Hello, caisse!"
    return render_template("index.html", billets=BILLETS, pieces=PIECES)

if __name__ == "__main__":
    app.run(debug=True)
    