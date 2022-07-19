##### IMPORT STATEMENTS
from flask import Flask, jsonify, render_template
import requests
import random


##### MAIN VARIABLES
app = Flask(__name__)
# link for real elephant API
url_all = 'https://elephant-api.herokuapp.com/elephants'


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Display info of a random elephant in a JSON format
@app.route('/random', methods=["POST", "GET"])
def random_ele_fun():
    # Request data from the website
    elephants = requests.get(url_all)
    elephants_data = elephants.json()

    # Randomly choose an elephant
    random_elephant = random.choice(elephants_data)
    return jsonify(elephant=random_elephant)


# Display info of all available elephants in a JSON format
@app.route('/all', methods=["POST", "GET"])
def all_elephants():
    elephants = requests.get(url_all)
    elephants_data = elephants.json()
    return jsonify(elephant=elephants_data)


# --- RUN THE API --- #
if __name__ == '__main__':
    app.run(debug=True)
