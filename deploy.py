from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render default port is 10000
    app.run(host="0.0.0.0", port=port, debug=True)