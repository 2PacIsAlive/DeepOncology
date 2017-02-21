from www import app
from flask import request, jsonify
import hmac
import hashlib
import subprocess


@app.route('/ci/webhook', methods=['POST'])
def github_ci_webhook():
    """

    Adapted from: https://github.com/Leo-G/Flask-Github-Webhooks-Handler
    """
    def verify_hmac_hash(data, signature):
        mac = hmac.new(app.config['GITHUB_SECRET'], msg=data, digestmod=hashlib.sha1)
        print type(mac.hexdigest())
        print type(signature)
        return hmac.compare_digest('sha1=' + mac.hexdigest(), signature.encode('utf-8'))

    signature = request.headers.get('X-Hub-Signature')
    data = request.data
    if verify_hmac_hash(data, signature):
        if request.headers.get('X-GitHub-Event') == "ping":
            return jsonify({'msg': 'Ok'})
        if request.headers.get('X-GitHub-Event') == "push":
            payload = request.get_json()
            if payload['commits'][0]['distinct']:
                try:
                    cmd_output = subprocess.check_output(
                        ['git', 'pull', 'origin', 'master'],)
                    return jsonify({'msg': str(cmd_output)})
                except subprocess.CalledProcessError as error:
                    return jsonify({'msg': str(error.output)})
    else:
        return jsonify({'msg': 'invalid hash'})