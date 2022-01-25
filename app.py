from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1><center>Flask Application Version 4</h1></center>"


app.run(host='0.0.0.0', port=5000)
