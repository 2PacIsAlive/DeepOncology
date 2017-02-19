from www import app
from flask import request, jsonify
from datetime import date

@app.route('/build', methods=["POST"])
def build():
    if request.json is None or len(request.json) < 1:
        return jsonify(
            type="error",
            message="Must provide a json network config in the request."
        ), 400
    else:
        network_config = request.json
        print network_config
        return jsonify(
            type="success",
            message="Network built successfully at {}.".format(date.today().isoformat())
        ), 200
