import json
from app.ai_service import generate_ai_response

def generate_proposal(client_type, budget):

    prompt = f"""
Create a sustainable B2B product proposal.

Client type: {client_type}
Budget: {budget}

Return ONLY valid JSON in this format:

{{
 "product_mix": ["product1","product2","product3"],
 "budget_allocation": {{
   "product1": 1000,
   "product2": 2000,
   "product3": 2000
 }},
 "impact_summary": "short sustainability impact summary"
}}
"""

    response = generate_ai_response(prompt)

    try:
        return json.loads(response)
    except:
        # fallback response if AI fails
        return {
            "product_mix": [
                "bamboo toothbrush",
                "organic cotton towels",
                "steel water bottles"
            ],
            "budget_allocation": {
                "toothbrush": 1000,
                "towels": 2500,
                "bottles": 1500
            },
            "impact_summary": "Using sustainable products reduces plastic waste and supports eco-friendly businesses."
        }