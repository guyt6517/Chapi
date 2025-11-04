from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chairupdate', methods=['POST'])
def update():
    data = request.get_json().get('status')

    # If the incoming JSON is a list, take the first element

    with open("data.txt", "w") as f:
        f.write(str(data))

    return jsonify({"status": "ok"}), 200


@app.route('/chairget', methods=['GET'])
def ret():
    try:
        with open("data.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = ""

    return jsonify({"status": data})


if __name__ == '__main__':
    app.run(debug=True)
