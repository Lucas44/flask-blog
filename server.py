from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def intro_page():
    return render_template("index.html")

@app.route("/newpage")
def new_page():
    return "<h1>This is a New Page Change two<h1/>"

if __name__=='__main__':
    app.run(debug=True)

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/account")
def account_page():
    return render_template("account.html")