from random import randint
from nltk.corpus import stopwords, brown
from flask import Blueprint, request, jsonify

word_bp = Blueprint('random-words', __name__)

stopwords_set = set(stopwords.words('english'))
brown_set = set(brown.words())

diff_set = brown_set.difference(stopwords_set)
diff_set = {e.lower() for e in diff_set if e.isalpha()}

global_words = list(diff_set)

@word_bp.route('/', strict_slashes=False)
def get_random_words():
    word_length = int(request.args.get('word_length', 0))
    num_of_words = int(request.args.get('num_of_words', 4))
    num_of_words = min(num_of_words, 12)
    starts_with = request.args.get('starts_with', '').lower()
    
    words = global_words

    filter_ = None
    if word_length and starts_with:
        filter_ = lambda w: len(w) == word_length and w.startswith(starts_with)
    elif word_length:
        filter_ = lambda w: len(w) == word_length
    elif starts_with:
        filter_ = lambda w: w.startswith(starts_with)
    
    if filter_:
        words = [w for w in words if filter_(w)]
    
    if len(words) < num_of_words:
        return jsonify(words)

    result = set()
    while len(result) < num_of_words:
        idx = randint(0, len(words) - 1)
        result.add(words[idx])

    return jsonify(list(result))


