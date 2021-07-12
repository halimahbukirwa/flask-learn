from flask import Flask, redirect , url_for


app = Flask(__name__)

#defining pages on our website

@app.route("/home") #decorating the function
def home():
    return "Hello, Welcome to the home page. <h1>Home Page </h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}. You're welcome"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) #redirecting


if __name__ == "__main__":
    app.run()