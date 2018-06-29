from flask import Flask, jsonify, request

import subprocess

app = Flask(__name__)


@app.route("/codingcount", methods=['POST'])
def github_webhook():
    if request.headers.get("X-GitHub-Event") == "ping":
        return jsonify({'msg': 'ok'})
    if request.headers.get("X-GitHub-Event") == "push":
        try:
            cmd_output = subprocess.check_output(
                ['git', 'pull', 'origin', 'master'],)
            return jsonify({'msg': str(cmd_output)})
        except Exception as e:
            return jsonify({'msg': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
