import os

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    if "FLASK_CONFIG" in os.environ:
        app.config.from_object(os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('lumen.settings.LocalConfig')

    @app.route('/')
    def hello():
        return jsonify({'message': 'hello joshua', 'foo': app.config['FOO']})

    return app

