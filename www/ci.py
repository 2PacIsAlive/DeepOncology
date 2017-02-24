from www import app
from flask import request, jsonify
import hmac
import hashlib

# TODO use subdomain="ci"

@app.route('/webhook', methods=['POST'])
def github_ci_webhook():
    """Github commit hook.

    Responds to github pings and pushes.

    Adapted from: https://github.com/Leo-G/Flask-Github-Webhooks-Handler
    """
    def verify_hmac_hash(data, signature):
        """Validate the hash signature in a request.

        This makes it possible to guarantee requests come from Github.
        Requires the GITHUB_SECRET environment variable to be set.

        Args:
            data (string): The request data.
            signature (string): The request X-Hub-Signature header.

        Returns:
            bool: A boolean indicating whether or not the request signature is valid.
        """
        mac = hmac.new(app.config['GITHUB_SECRET'], msg=data, digestmod=hashlib.sha1)
        return hmac.compare_digest('sha1=' + mac.hexdigest(), signature.encode('utf-8'))

    signature = request.headers.get('X-Hub-Signature')
    data = request.data
    if verify_hmac_hash(data, signature):
        if request.headers.get('X-GitHub-Event') == 'ping':
            return jsonify({'message': 'Thanks for the ping, bae.'})
        if request.headers.get('X-GitHub-Event') == 'push':
            payload = request.get_json()
            if payload['commits'][0]['distinct']:
                # TODO something
                print payload
                return jsonify({'message': 'Oh what an interesting push.'})
    else:
        return jsonify({'message': 'Invalid hash :('})
