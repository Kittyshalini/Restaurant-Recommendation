from flask import Flask, render_template, request
from recommend import recommend

app = Flask(__name__)

import pickle

df = pickle.load(open('data.pkl','rb'))

@app.route('/')

def index():
    name = sorted(df['name'].values)
    return render_template("index.html", name = name)

@app.route('/predict', methods=['GET'])
def predict():
    user_input = request.args.get('name')

    if not user_input:
        return render_template("index.html", name=sorted(df['name'].unique()), error="Please select a restaurant.")

    recs = recommend(user_input)

    if not recs:
        return render_template("index.html", name=sorted(df['name'].unique()), error="No recommendations found.")

    return render_template("index.html", name=sorted(df['name'].unique()), recs=recs, selected=user_input)

if __name__ == '__main__':
    app.run(debug=True)