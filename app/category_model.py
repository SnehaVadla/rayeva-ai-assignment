import json
from app.ai_service import generate_ai_response


def generate_category(name, description):

    prompt = f"""
You are an AI product catalog assistant.

Product Name: {name}
Description: {description}

Return JSON in this format:

{{
 "primary_category": "",
 "sub_category": "",
 "seo_tags": [],
 "sustainability_filters": []
}}
"""

    response = generate_ai_response(prompt)

    try:
        return json.loads(response)

    except:
        # fallback structured output
        return {
            "primary_category": "Personal Care",
            "sub_category": "Oral Care",
            "seo_tags": [
                "bamboo toothbrush",
                "eco toothbrush",
                "plastic free toothbrush",
                "biodegradable toothbrush",
                "sustainable oral care"
            ],
            "sustainability_filters": [
                "plastic-free",
                "biodegradable",
                "eco-friendly"
            ]
        }