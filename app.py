from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/chairupdate', methods = ['POST'])
def update():
  data = request.get_json
