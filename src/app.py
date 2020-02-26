from flask import Flask, jsonify, request

from blueprints.hash import hash_bp
from blueprints.randomwords import word_bp

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(hash_bp, url_prefix='/hash')
app.register_blueprint(word_bp, url_prefix='/random-words')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


