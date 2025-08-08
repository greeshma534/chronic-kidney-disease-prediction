import numpy as np
import joblib

# Load the trained Random Forest model
rf_model = joblib.load('rf_model.pkl')

# Define the input data
input_data = np.array([[1.025,6.9,947,28.4,395,2.64]])

# Make predictions
predictions = rf_model.predict(input_data)

# Print predictions
print("Predicted class:", predictions[0])
