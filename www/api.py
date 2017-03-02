from www import app
from flask import request, jsonify
from datetime import date
import sys

sys.path.append("..")  # hack because haven't packages up deep_networks yet
from deep_networks.network.build import NetworkBuilder
from deep_networks.network.config import NetworkConfig

# TODO use subdomain="api"

@app.route('/build', methods=["POST"])#, subdomain="api")
def build():
    if request.json is None or len(request.json) < 1:
        return jsonify(
            type="error",
            message="Must include at least one layer."
        ), 400
    else:
        print request.json
        try:
        network = NetworkBuilder().build_from_config(request.json)
        print network
        return jsonify(
            type="success",
            message="Network built successfully at {}.".format(date.today().isoformat())
        ), 200
