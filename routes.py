# import Flask class and render function
from flask import Flask, render_template

# create a new usable instance of the flask class and save it into variable app
app = Flask(__name__)

# map URL to flask function
@app.route('/')
    # here / is mapped to the index function
def index():
    # python function uses render_template function to return index.html
    return render_template("index.html")

@app.route('/about')
    # map url about to python function about
def about():
    # python function uses render_template function to return about.html
    return render_template("about.html")


    # turn on debug=true to see error messages
if __name__ == "__main__":
    app.run(debug=True)
