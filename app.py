from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    news_text = ""

    if request.method == 'POST':
        news_text = request.form['news']

        # Convert text into vector
        data = [news_text]
        vect = vectorizer.transform(data)

        # Make prediction
        prediction = model.predict(vect)[0]

    return render_template(
        'index.html',
        prediction=prediction,
        news_text=news_text
    )


if _name_ == '_main_':
    app.run(debug=False, host='0.0.0.0') # debug False kar