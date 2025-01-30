from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def get_details():
    return jsonify({
        'email': 'rhodalee.dev@gmail.com',
        'current_datetime' : datetime.utcnow().isoformat() + 'Z',
        'github_url' : 'https://github.com/rhoda-lee/hng12-internship'
    }), 200


if __name__ == '__main__':
    app.run()