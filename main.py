from flask import Flask, jsonify, render_template
import requests
import random

app = Flask(__name__)

url_all = 'https://elephant-api.herokuapp.com/elephants'


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=["POST", "GET"])
def random_ele_fun():
    elephants = requests.get(url_all)
    elephants_data = elephants.json()
    random_elephant = random.choice(elephants_data)
    return jsonify(elephant=random_elephant)


@app.route('/all', methods=["POST", "GET"])
def all_cafes():
    elephants = requests.get(url_all)
    elephants_data = elephants.json()
    return jsonify(elephant=elephants_data)


if __name__ == '__main__':
    app.run(debug=True)
