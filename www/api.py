from www import app
from flask import request, jsonify
from datetime import date

# TODO use subdomain="api"

@app.route('/build', methods=["POST"], subdomain="api")
def build():
    if request.json is None or len(request.json) < 1:
        return jsonify(
            type="error",
            message="Must include at least one layer."
        ), 400
    else:
        network_config = request.json
        print network_config
        return jsonify(
            type="success",
            message="Network built successfully at {}.".format(date.today().isoformat())
        ), 200
