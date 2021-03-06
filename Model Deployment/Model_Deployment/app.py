from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model/modelfp1.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('main.html', prediction_text='Prediksi Tarif yaitu $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)