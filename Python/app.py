import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    #print(data)
    l1= list(data)
    result =[]
    '''
    print('Length is ', len(l1))
    print('Key-Value', l1[0])
    print('Value is ',l1[0].values())
    '''
    for i in range(len(l1)):
        prediction = model.predict([np.array(list(l1[i].values()))])
        result.append(prediction[0])
        

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)