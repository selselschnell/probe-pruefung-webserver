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
    url = "https://www.w3schools.com/cssref/css_selectors.asp"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# select your objects
table_rows = [elem for elem in soup.select('.ws-table-all tr')]


# apply filter function
table_rows = list(filter(my_filter, table_rows))


# create the structure for the json file
selectors = []

for row in table_rows:
    cells = list(row.select('td'))
    if cells:
        entry = {
            'selector': "placeholder text, which will be overwritten below",
            'example': cells[1].text,
            'description': cells[2].text,
            
        }
        # we need the following code beacause not all entries in the first column are text - some are links (a-tag)
        if cells[0].a:
            entry['selector'] = cells[0].a.text
        else:
            entry['selector'] = cells[0].text

        selectors.append(entry)
        write_json(selectors)


# filter function
def my_filter(elem):
  return True

# output to json
def write_json(selectors): 
with open("selectors.json", 'w') as f:
    json.dump(selectors, f, indent=4)
    
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
