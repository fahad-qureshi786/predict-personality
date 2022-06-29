import clf as clf
import numpy as np
import vect
from flask import Flask, render_template, request, redirect, url_for
# from wtforms import Form, TextAreaField, validators
import pickle
import os

from gensim.parsing import remove_stopwords
from google.protobuf.text_format import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from nltk import WordNetLemmatizer

# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
from gensim.parsing.preprocessing import remove_stopwords
import re
from string import digits
import string


#
# from vectorizer import vect
from wtforms import TextAreaField, validators, Form

app = Flask(__name__)
""" Form Handling """


cur_dir = os.path.dirname(__file__)
cv = pickle.load(open(os.path.join(cur_dir,'','Personality_Prediction.pkl'), 'rb'))

def classify(document):
    label = {'INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
       'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ'}
    X = vect.transform([document])
    # Preprocess

    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba

######## Preparing the Classifier
# cur_dir = os.path.dirname(__file__)
# clf = pickle.load(open(os.path.join(cur_dir,
#                  'pkl_objects',
#                  'classifier.pkl'), 'rb'))
# db = os.path.join(cur_dir, 'reviews.sqlite')

# def classify(document):
#     label = {'negative': 'negative', 'positive': 'positive'}
#     X = vect.transform([document])
#     y = clf.predict(X)[0]
#     proba = np.max(clf.predict_proba(X))
#     return label[y], proba
#
# def train(document, y):
#     X = vect.transform([document])
#     clf.partial_fit(X, [y])
#
# def sqlite_entry(path, document, y):
#     conn = sqlite3.connect(path)
#     c = conn.cursor()
#     c.execute("INSERT INTO review_db (review, sentiment, date)"\
#     " VALUES (?, ?, DATETIME('now'))", (document, y))
#     conn.commit()
#     conn.close()
#
# ######## Flask
# class ReviewForm(Form):
#     moviereview = TextAreaField('',
#                                 [validators.DataRequired(),
#                                 validators.length(min=15)])

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
