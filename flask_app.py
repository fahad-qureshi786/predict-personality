from flask import Flask, render_template, request
# from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np

from vectorizer import vect

app = Flask(__name__)

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
    form = ReviewForm(request.form)
    return render_template('index.html', form=form)

@app.route('/about', methods=['POST'])
def feedback():
    # feedback = request.form['feedback_button']
    # review = request.form['review']
    # prediction = request.form['prediction']
    #
    # inv_label = {'negative': 'negative', 'positive': 'positive'}
    # y = inv_label[prediction]
    # if feedback == 'Incorrect':
    #     y = int(not(y))
    # train(review, y)
    # sqlite_entry(db, review, y)
    return render_template('code.html')

@app.route('/code', methods=['POST'])
def feedback():
    # feedback = request.form['feedback_button']
    # review = request.form['review']
    # prediction = request.form['prediction']
    #
    # inv_label = {'negative': 'negative', 'positive': 'positive'}
    # y = inv_label[prediction]
    # if feedback == 'Incorrect':
    #     y = int(not(y))
    # train(review, y)
    # sqlite_entry(db, review, y)
    return render_template('code.html')



if __name__ == '__main__':
    app.run(debug=True)