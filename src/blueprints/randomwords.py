from random import randint
from nltk.corpus import stopwords, brown
from flask import Blueprint, request, jsonify

word_bp = Blueprint('random-words', __name__)

stopwords_set = set(stopwords.words('english'))
brown_set = set(brown.words())
brown_set = brown_set.difference(stopwords_set)

global_words = list(brown_set)
global_words = [w for w in global_words if w.isalpha()]

@word_bp.route('/', strict_slashes=False)
def get_random_words():
    word_length = int(request.args.get('word_length', 0))
    num_of_words = int(request.args.get('num_of_words', 4))
    num_of_words = min(num_of_words, 12)
    starts_with = request.args.get('starts_with')
    
    words = global_words

    if word_length > 0:
        words = [w for w in words if len(w) == word_length]

    if starts_with:
        words = [w for w in words if w.startswith(starts_with)]

    result = []
    for _ in range(num_of_words):
        idx = randint(0, len(words) - 1)
        result.append(words[idx])

    return jsonify(result)


