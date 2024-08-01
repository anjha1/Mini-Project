from flask import Flask, request, jsonify, render_template
import ibm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    array_of_values_to_be_scored = [
        [data['day'], data['month'], data['year'], data['Temperature'], data['RH'], data['Ws'], data['Rain'], data['FFMC'], data['DMC'], data['DC'], data['ISI'], data['BUI'], "not fire", data['Region']]
    ]
    
    result = ibm.score_data(array_of_values_to_be_scored)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
