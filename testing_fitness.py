import pandas as pd
import joblib

# Load the saved model, scaler, encoders, and feature names
loaded_knn_model = joblib.load('knn_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')
loaded_label_encoders = joblib.load('label_encoders.pkl')
feature_names = joblib.load('feature_names.pkl')

print("Model, scaler, encoders, and feature names loaded successfully!\n")

# Provide user options and take input one by one
print("Enter the following options as numbers:")

# Sex input
sex_options = {1: 'Male', 2: 'Female'}
print("\nSelect your Sex:")
for k, v in sex_options.items():
    print(f"{k}: {v}")
sex = sex_options[int(input("\nEnter your choice for Sex (1/2): "))]

# Hypertension input
hypertension_options = {1: 'Yes', 2: 'No'}
print("\nSelect if you have Hypertension:")
for k, v in hypertension_options.items():
    print(f"{k}: {v}")
hypertension = hypertension_options[int(input("\nEnter your choice for Hypertension (1/2): "))]

# Diabetes input
diabetes_options = {1: 'Yes', 2: 'No'}
print("\nSelect if you have Diabetes:")
for k, v in diabetes_options.items():
    print(f"{k}: {v}")
diabetes = diabetes_options[int(input("\nEnter your choice for Diabetes (1/2): "))]

# Level input
level_options = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced'}
print("\nSelect your Fitness Level:")
for k, v in level_options.items():
    print(f"{k}: {v}")
level = level_options[int(input("\nEnter your choice for Level (1/2/3): "))]

# Fitness goal input
fitness_goal_options = {1: 'Weight Loss', 2: 'Strength', 3: 'Endurance'}
print("\nSelect your Fitness Goal:")
for k, v in fitness_goal_options.items():
    print(f"{k}: {v}")
fitness_goal = fitness_goal_options[int(input("\nEnter your choice for Fitness Goal (1/2/3): "))]

# Fitness type input
fitness_type_options = {1: 'Cardio', 2: 'Strength Training', 3: 'Flexibility'}
print("\nSelect your Fitness Type:")
for k, v in fitness_type_options.items():
    print(f"{k}: {v}")
fitness_type = fitness_type_options[int(input("\nEnter your choice for Fitness Type (1/2/3): "))]

# Numerical inputs
age = int(input("\nEnter your Age (in years): "))
height = float(input("Enter your Height (in cm): "))
weight = float(input("Enter your Weight (in kg): "))
bmi = weight / ((height / 100) ** 2)  # Calculate BMI automatically

# Display input summary
print(f"\nSummary of Your Inputs:\nSex: {sex}\nHypertension: {hypertension}\nDiabetes: {diabetes}\nLevel: {level}\nFitness Goal: {fitness_goal}\nFitness Type: {fitness_type}")
print(f"Age: {age}\nHeight: {height} cm\nWeight: {weight} kg\nBMI: {bmi}")

# Create a DataFrame for the input data
new_data = pd.DataFrame({
    'Age': [age],
    'Height': [height],
    'Weight': [weight],
    'BMI': [bmi],
    'Sex': [sex],
    'Hypertension': [hypertension],
    'Diabetes': [diabetes],
    'Level': [level],
    'Fitness Goal': [fitness_goal],
    'Fitness Type': [fitness_type]
})

# Encode the categorical columns in the new data
categorical_columns = ['Sex', 'Hypertension', 'Diabetes', 'Level', 'Fitness Goal', 'Fitness Type']

for col in categorical_columns:
    encoder = loaded_label_encoders[col]
    # Handle unseen labels by mapping to a default class if necessary
    new_data[col] = new_data[col].apply(lambda x: x if x in encoder.classes_ else encoder.classes_[0])
    new_data[col] = encoder.transform(new_data[col])

# Reorder columns to match feature names used during training
new_data = new_data[feature_names]

# Scale the new data
new_data_scaled = loaded_scaler.transform(new_data)

# Predict using the loaded model
new_prediction = loaded_knn_model.predict(new_data_scaled)

# Print the prediction
print(f"\nRecommended Exercise for you: {new_prediction[0]}")
