from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def intro_page():
    return render_template("home.html")

@app.route("/newpage")
def new_page():
    return "<h1>This is a New Page Change two<h1/>"

@app.route("/account")
def account_page():
    return render_template("account.html")

@app.route("/main")
def main_page():
    return render_template("main.html")

if __name__=='__main__':
    app.run(debug=True)