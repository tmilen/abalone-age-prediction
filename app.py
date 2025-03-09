import pickle
import numpy as np
import os
from flask import Flask,render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app =Flask(__name__)
    client=MongoClient(os.getenv("MONGODB_URI"))
    app.db=client.abalone
    
    model_path = "./rf_model.pkl"
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    sex_mapping = {'M': 0, 'F': 1, 'I': -1}
    @app.route("/",methods=['GET',"POST"])
    def home():
        prediction = None

        if request.method == "POST":
            try:
                # Get form data
                sex = request.form["sex"]
                length = float(request.form["length"])
                diameter = float(request.form["diameter"])
                height = float(request.form["height"])
                whole_weight = float(request.form["whole_weight"])
                shucked_weight = float(request.form["shucked_weight"])
                viscera_weight = float(request.form["viscera_weight"])
                shell_weight = float(request.form["shell_weight"])

                # Convert categorical "Sex" to numeric
                sex_numeric = sex_mapping[sex]

                # Prepare input data
                input_data = np.array([[sex_numeric, length, diameter, height, whole_weight,
                                        shucked_weight, viscera_weight, shell_weight]])

                # Make prediction
                predicted_age = model.predict(input_data)[0]
                predicted_age = round(predicted_age, 2)  # Round for readability

                # Save prediction to MongoDB
                prediction_data = {
                    "sex": sex,
                    "length": length,
                    "diameter": diameter,
                    "height": height,
                    "whole_weight": whole_weight,
                    "shucked_weight": shucked_weight,
                    "viscera_weight": viscera_weight,
                    "shell_weight": shell_weight,
                    "predicted_age": predicted_age
                }
                app.db.prediction.insert_one(prediction_data)

                # Set the prediction result for the UI
                prediction = predicted_age

            except Exception as e:
                print(f"Error during prediction: {e}")
                prediction = "Error in prediction"

        return render_template("home.html", prediction=prediction)

    return app

