import json
from app.ai_service import generate_ai_response

def generate_impact(product_name, quantity):

    # Business logic calculations
    avg_plastic_weight = 0.02  # kg plastic per product
    emission_factor = 6        # kg CO2 per kg plastic

    plastic_saved = quantity * avg_plastic_weight
    carbon_avoided = plastic_saved * emission_factor

    prompt = f"""
Generate a sustainability impact report.

Product: {product_name}
Quantity: {quantity}

Plastic saved: {plastic_saved} kg
Carbon avoided: {carbon_avoided} kg CO2

Return JSON:

{{
 "plastic_saved": number,
 "carbon_avoided": number,
 "impact_statement": "short sustainability statement"
}}
"""

    response = generate_ai_response(prompt)

    try:
        data = json.loads(response)
        return data
    except:
        return {
            "plastic_saved": plastic_saved,
            "carbon_avoided": carbon_avoided,
            "impact_statement": "This order contributes to reducing plastic waste and lowering carbon emissions."
        }