from flask import Flask, render_template

app = Flask(__name__)

@app.get("/<fizzbuzz>")
def index(fizzbuzz):
    return render_template("index.html", fizzbuzz=fizzbuzz)