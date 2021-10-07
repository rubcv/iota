from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/send', methods=['POST'])
def send():
    # Send the transaction to the Tangle
    return request.json

@app.route('/api/v1/meeting/<id>', methods=['GET'])
def get_meeting(id):
    # Query from the Tangle
    return id


@app.route('/api/v1/user/<id>', methods=['GET'])
def get_user(id):
    # Query from the Tangle
    return id

# Accept connections from outside Docker
app.run(host="0.0.0.0")
