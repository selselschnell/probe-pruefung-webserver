#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)


# webscraping function
def my_scraper():
    # YOUR CODE GOES HERE
    pass


# filter function
def my_filter():
    # YOUR CODE GOES HERE
    pass

# output to json
def write_json():
    # YOUR CODE GOES HERE
    pass


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/css-selectors")
def css_selectors():
    return render_template("css-selectors.html", selectors=load_selectors())


# starts the webserver
if __name__ == "__main__":
    app.run()
