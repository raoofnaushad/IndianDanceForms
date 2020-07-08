from flask import Flask, jsonify, request
import predict

app = Flask(__name__)

MODEL = None
DEVICE = None

@app.route('/classify', methods=['POST'])
def classify():
    response = request.files['file']
    file_name = response.filename
    response.save('check/image.jpg')
    result = predict.predict_single()
    response = {
        "Type": result
    }
    return jsonify(response)



if __name__ == "__main__":
    app.run(debug=True, port=1234)