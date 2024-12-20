from flask import Flask
from predict_organization_rate import predict_organization_rate, predict_all_organization_rate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, ngrok. Ayo belajar AI !"
# 
@app.route('/predict/<organization_code>', methods=['PUT'])
def predict(organization_code):
    result = predict_organization_rate(organization_code, 12)
    
    if result == "Success" or result == "Data with the same last_payment already exists, skipping insert.":
        return {"status": True, "message": result}
    else:
        return {"status": False, "message": result}
    
@app.route('/predict-all', methods=['PUT'])
def predict_all():
    result = predict_all_organization_rate(12)
    
    if result == "Success":
        return {"status": True, "message": result}
    else:
        return {"status": False, "message": result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
