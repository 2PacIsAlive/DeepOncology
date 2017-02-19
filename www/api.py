from www import app
from flask import request, jsonify

@app.route('/build', methods=["POST"])
def build():
    if request.json is None:
        return jsonify(
            type="error",
            message="Must provide a json network config in the request."
        ), 400
    else:
        network_config = request.json
        print network_config
        return jsonify(
            type="success",
            message="Network built successfully at 10:52:01 PM, Sat Feb 18."
        ), 200