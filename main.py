import joblib
import pandas as pd

def load_model_and_encoders(model_path, encoders_path):
    """Load the trained model and label encoders."""
    model = joblib.load(model_path)
    encoders = joblib.load(encoders_path)
    return model, encoders

def prepare_input_data(input_data, encoders):
    """Encode input data using the provided label encoders."""
    for column, encoder in encoders.items():
        if column in input_data:
            try:
                input_data[column] = encoder.transform([input_data[column]])[0]
            except ValueError:
                raise ValueError(
                    f"The input value '{input_data[column]}' for '{column}' is not recognized. "
                    f"Ensure the encoder was trained with this value."
                )
    return input_data

def predict_exercise(model, encoders, input_data):
    """Predict exercises based on input data."""
    # Prepare input data as a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make predictions
    prediction = model.predict(input_df)[0]

    # Decode the prediction back to the original label
    exercise_decoder = encoders['Exercises']
    decoded_prediction = exercise_decoder.inverse_transform([prediction])[0]
    return decoded_prediction

def get_user_input(encoders):
    """Collect input data from the user interactively."""
    input_data = {}
    print("Enter the following details:")

    # Define mappings for numeric choices based on your dataset
    sex_mapping = {"1": "Male", "2": "Female"}
    hypertension_mapping = {"1": "Yes", "2": "No"}
    diabetes_mapping = {"1": "Yes", "2": "No"}
    level_mapping = {"1": "Underweight", "2": "Normal", "3": "Overweight", "4": "Obese"}
    fitness_goal_mapping = {"1": "Weight Loss", "2": "Weight Gain", "3": "Endurance"}
    fitness_type_mapping = {"1": "Cardio", "2": "Strength", "3": "Flexibility"}
    equipment_mapping = {"1": "Treadmill", "2": "Dumbbells", "3": "Resistance Bands"}
    diet_mapping = {"1": "Balanced", "2": "High-Protein", "3": "Low-Carb"}

    input_data["Sex"] = sex_mapping[input("1: Male, 2: Female\nEnter Sex (1/2): ")]
    input_data["Age"] = int(input("Enter Age: "))
    input_data["Height"] = float(input("Enter Height (in meters): "))
    input_data["Weight"] = float(input("Enter Weight (in kg): "))
    input_data["Hypertension"] = hypertension_mapping[input("1: Yes, 2: No\nHypertension (1/2): ")]
    input_data["Diabetes"] = diabetes_mapping[input("1: Yes, 2: No\nDiabetes (1/2): ")]
    input_data["BMI"] = float(input("Enter BMI: "))
    input_data["Level"] = level_mapping[input("1: Underweight, 2: Normal, 3: Overweight, 4: Obese\nEnter Level (1/2/3/4): ")]
    input_data["Fitness Goal"] = fitness_goal_mapping[input("1: Weight Loss, 2: Weight Gain, 3: Endurance\nEnter Fitness Goal (1/2/3): ")]
    input_data["Fitness Type"] = fitness_type_mapping[input("1: Cardio, 2: Strength, 3: Flexibility\nEnter Fitness Type (1/2/3): ")]
    input_data["Equipment"] = equipment_mapping[input("1: Treadmill, 2: Dumbbells, 3: Resistance Bands\nEnter Equipment (1/2/3): ")]
    input_data["Diet"] = diet_mapping[input("1: Balanced, 2: High-Protein, 3: Low-Carb\nEnter Diet (1/2/3): ")]
    return input_data

# Paths to your saved model and encoders
model_path = 'exercise_prediction_model.pkl'
encoders_path = 'label_encoders.pkl'

# Load the model and encoders
model, encoders = load_model_and_encoders(model_path, encoders_path)

# Collect user input
data_from_user = get_user_input(encoders)

# Encode input data1

input_data_encoded = prepare_input_data(data_from_user, encoders)

# Predict the exercise
predicted_exercise = predict_exercise(model, encoders, input_data_encoded)
print("Predicted Exercise:", predicted_exercise)
