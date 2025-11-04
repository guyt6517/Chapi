from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/chairupdate', methods = ['POST'])
def update():
  data = request.get_json()[0]
  with open("data.txt", "w") as f:
    f.write(data)

@app.route('/chairget', methods = ['GET'])
def ret():
  with open("data.txt", "r") as f:
    data = f.read()
  return jsonify({
    "status": data
  })

if __name__ == '__main__':
  app.run(debug = True)
