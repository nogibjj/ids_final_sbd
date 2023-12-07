from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/red")
def red():
    return render_template("color.html", color="red")

@app.route("/blue")
def blue():
    return render_template("color.html", color="blue")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)