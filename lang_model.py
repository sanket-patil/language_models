import kenlm
from flask import Flask, jsonify, request
import urllib


LANG_MODEL = 'hi_wiki.klm'
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/lm_score/', methods=['GET', 'POST'])
def get_score():
    candidates = request.args.get('candidates')
    model = kenlm.LanguageModel(LANG_MODEL)
    scores = dict()
    candidates = [candidate.strip() for candidate in candidates.split(',')]
    for candidate in candidates:
        scores[candidate] = model.score(candidate)
    return jsonify(scores)
    #return jsonify({'status': 'ok', 'candidates': candidates})
