from flask import Flask, render_template

app = Flask(__name__)

BILLETS = [100, 50, 20, 10, 5]

@app.route("/")
def index():
    # return "Hello, caisse!"
    return render_template("index.html", billets=BILLETS)

if __name__ == "__main__":
    app.run(debug=True)
    