from Feature_Extractor import extract_features
import requests
import json
# ------------------------------------------------------------------------

# This function takes the url and returns probability value

def get_prediction(url):
    # URL of the hosted model
    model_url = "https://tensorflow-serve.onrender.com/v1/models/Malicious_URL_Prediction:predict"

    # Extract features from the URL
    print("Extracting features from URL...")
    url_features = extract_features(url)
    print(url_features)

    # Prepare the data for the prediction request
    payload = {
        "signature_name": "serving_default",
        "instances": [url_features]
    }

    headers = {"Content-Type": "application/json"}

    # Make the prediction request to the hosted model
    print("Making prediction...")
    response = requests.post(model_url, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        prediction = response.json()
        # Extract prediction (assuming the model returns a prediction in 'predictions')
        prediction_value = prediction['predictions'][0][0]
        
        # Calculate and print the result
        i = prediction_value * 100
        i = round(i, 3)
        print("There is ", i, "% chance, the URL is malicious!")

        return i
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return 0
