
from flask import Flask, render_template, request, jsonify

from model import predict_medicine
from llm_chain import chains, predict_chain

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/krushi")
def krushi():
    return render_template("krushi.html")

@app.route("/sale")
def sale():
    return render_template("sale.html")

@app.route("/machines")
def machines():
    return render_template("machines.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/reel")
def reel():
    return render_template("reel.html")

@app.route('/predict', methods=['POST'])
def predict_app():
    crop = request.form.get("crop")
    problem = request.form.get("problem")
    weather = request.form.get("weather")
    soil = request.form.get("soil")
    stage = request.form.get("stage")
    severity = request.form.get("severity")

    input_data = [[crop, problem, weather, soil, stage, severity]]

    prediction = predict_medicine(input_data)

    chatbot_rep = predict_chain.invoke({
        'crop': crop,
        'problem': problem,
        'weather': weather,
        'soil': soil,
        'stage': stage,
        'severity': severity,
        'prediction': prediction
    })

    return render_template(
        "predict.html",
        crop=crop,
        problem=problem,
        weather=weather,
        soil=soil,
        stage=stage,
        severity=severity,
        prediction=prediction,
        suggestion=chatbot_rep
    )


@app.route("/get", methods=['POST'])
def get_bot_response():
    user_input = request.json.get("message")
    result = chains.invoke({'input': user_input}, config={"timeout": 10})
    return jsonify({"reply": result})


if __name__ == "__main__":
    app.run(debug=True)