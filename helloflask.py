from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    print "First time running Flask !! "
    return "Hello World! \t \t    \t    Hello Flask      !!"


if __name__ == "__main__":
    app.run()
