# README
# This script uses the Google Vision API to analyze the content of an image and outputs the results as a JSON file.
# Requirements:
# - A Google Vision API key
# - The `requests` Python library (install via `pip install requests`)
#
# How to use:
# 1. Replace `your_api_key_here` with your Google Vision API key.
# 2. Set the `image_path` variable to the path of the image you want to analyze.
# 3. Run the script. The results will be saved in a JSON file named `image_analysis_results.json`.

import requests
import base64
import json

def analyze_image(api_key, image_path, output_file="image_analysis_results.json"):
    """
    Analyzes the content of an image using Google Vision API and saves the result as a JSON file.

    Args:
        api_key (str): Your Google Vision API key.
        image_path (str): Path to the image file.
        output_file (str): Path to the output JSON file.

    Returns:
        None
    """
    # URL for the Vision API
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"

    # Read and encode the image as Base64
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Prepare the payload
    payload = {
        "requests": [
            {
                "image": {"content": encoded_image},
                "features": [{"type": "LABEL_DETECTION", "maxResults": 10}],
            }
        ]
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    # Check for errors
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, {response.text}")

    # Parse the response JSON
    response_data = response.json()

    # Save the result to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(response_data, json_file, indent=4)

    print(f"Analysis results saved to {output_file}")

if __name__ == "__main__":
    # Your Google Vision API key
    api_key = "change_api_key"

    # Path to the image to analyze
    image_path = "image.png"

    # Output file for the JSON result
    output_file = "image_analysis_results.json"

    # Analyze the image and save the results
    try:
        analyze_image(api_key, image_path, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
