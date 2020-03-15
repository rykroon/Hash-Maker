from flask import Flask, jsonify, request

from blueprints.hash import hash_bp
from blueprints.randomwords import word_bp
from blueprints.nounphrase import nounphrase_bp

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(hash_bp, url_prefix='/hash')
app.register_blueprint(word_bp, url_prefix='/random-words')
app.register_blueprint(nounphrase_bp, url_prefix='/noun-phrase')

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'endpoints': {
            '/hash': {
                'params': {
                    'q': 'The string to be hashed'
                }
            },
            '/random-words': {
                'params': {
                    'num_of_words': 'The number of words to be returned',
                    'word_length': 'The length of the words',
                    'starts_with': 'A substring that the words should start with'
                }
            },
            '/noun-phrase': {
                'params': {
                    'starts_with': 'A substring that the adjective and noun should start with.'
                }
            }
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


