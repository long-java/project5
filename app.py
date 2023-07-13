from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1'>Project 5. Pham Tien Long</h1>"


if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80