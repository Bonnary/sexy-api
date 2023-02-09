from flask import Flask
import json
import random
app = Flask(__name__)

d = json.load(open("data.json", "r"))


@app.route("/")
def hello_world():
    rannum = random.randint(1, len(d))
    return d[f"{rannum}"]


if __name__ == "__main__":
    app.run()
