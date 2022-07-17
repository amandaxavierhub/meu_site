from distutils.log import debug
from flask import Flask, render_template

#create app
app = Flask(__name__)

#def homepage

@app.route("/")
def homepage():
    return render_template("homepage.html")
    
#def contatos

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#def posts

@app.route("/posts")
def posts():
    return render_template("posts.html")


# start app
if  __name__ == "__main__":
    app.run(debug=True)