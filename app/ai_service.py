import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def generate_ai_response(prompt):

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, json=payload)

    result = response.json()

    # Case 1: normal response
    if isinstance(result, list):
        return result[0]["generated_text"]

    # Case 2: model loading
    if "error" in result:
        return "Eco Friendly Product"

    # Case 3: other structure
    if "generated_text" in result:
        return result["generated_text"]

    return "Eco Friendly Product"