from random import randint
from flask import Blueprint, request, jsonify
from nltk.corpus import wn

adjs = list(wn.all_lemma_names(wn.ADJ))
nouns = list(wn.all_lemma_names(wn.NOUN))

nounphrase_bp = Blueprint('noun-phrase', __name__)

@nounphrase_bp.route('/', methods=['GET'], strict_slashes=False)
def get_noun_phrase():
    starts_with = request.args.get('starts_with')
    
    temp_adjs = adjs 
    temp_nouns = nouns

    if starts_with:
        fltr = lambda s, lst: [e for e in lst if e.startswith(s)]
        temp_adjs = fltr(starts_with, temp_adjs)
        temp_nouns = fltr(starts_with, temp_nouns)

    idx = randint(0, len(temp_adjs) - 1)
    adj = temp_adjs[idx]

    idx = randint(0, len(temp_nouns) - 1)
    noun = temp_nouns[idx]

    return jsonify({'result': "{} {}".format(adj, noun)})

    