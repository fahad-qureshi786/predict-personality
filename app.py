import clf as clf
import numpy as np
import vect
from flask import render_template, request, redirect, url_for
import pickle
import os
from flask import Flask
app = Flask(__name__)
import os
import pickle
import re
from flask import Flask, request, jsonify
from nltk import WordNetLemmatizer
from tqdm import tqdm
cur_dir = os.path.dirname(__file__)
from sklearn.feature_extraction.text import HashingVectorizer
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from flask import Flask, request, jsonify


""" Rest API """
cv = pickle.load(open(os.path.join(cur_dir,'','model.pkl'), 'rb'))


def clear_text(data):
    data_length = []
    lemmatizer = WordNetLemmatizer()
    cleaned_text = []
    for sentence in tqdm(data):
        sentence = sentence.lower()

        #         removing links from text data
        sentence = re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+', ' ', sentence)

        #         removing other symbols
        sentence = re.sub('[^0-9a-z]', ' ', sentence)

        data_length.append(len(sentence.split()))
        cleaned_text.append(sentence)
    return cleaned_text


def process(document):
    document = clear_text(document)

    class Lemmatizer(object):
        def __init__(self):
            self.lemmatizer = WordNetLemmatizer()

        def __call__(self, sentence):
            return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word) > 2]

    vectorizer = HashingVectorizer(n_features=5000)

    post = vectorizer.transform(document).toarray()

    return post


@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    output = cv.predict(process([data]))
    map = {1: 'HCI', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'BBB', 7: 'EEE', 8: 'FFGG',
           9: 'AAAB', 10: 'LLL', 11: 'AAAA', 12: 'QQQ', 13: 'EEE', 14: 'AAA', 15: 'SSS', 16: 'GGG', }


    print(map.get(output[0]))

    return jsonify(map.get(output[0]))

def classify(document):
    label = {'INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
       'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ'}
    X = vect.transform([document])
    # Preprocess

    y = cv.predict(X)[0]
    proba = np.max(cv.predict_proba(X))
    return label[y], proba


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('about.html')


@app.route('/code', methods=['GET', 'POST'])
def code():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('code.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('contact.html')


@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('model.html')


@app.route('/personality', methods=['GET', 'POST'])
def personality():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('personality.html')


if __name__ == '__main__':
    app.run(debug=True)
