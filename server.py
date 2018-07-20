from flask import Flask
app = Flask(__name__)

@app.route("/")
def intro_page():
    return "Hello World!"

@app.route("/newpage")
def new_page():
    return "<h1>This is a New Page Change two<h1/>"

if __name__=='__main__':
    app.run(debug=True)