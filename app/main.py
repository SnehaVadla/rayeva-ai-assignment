from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from .models import Product, Proposal
from .category_model import generate_category
from .proposal_model import generate_proposal
from app.impact_model import generate_impact
from app.whatsapp_bot import generate_whatsapp_reply

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/generate-category")
def category_api(data: dict):

    name = data["name"]
    description = data["description"]

    result = generate_category(name, description)

    db = SessionLocal()

    product = Product(
        name=name,
        description=description,
        category=result.get("primary_category"),
        sub_category=result.get("sub_category"),
        tags=str(result.get("seo_tags")),
        filters=str(result.get("sustainability_filters"))
    )

    db.add(product)
    db.commit()

    return result


@app.post("/generate-proposal")
def proposal_api(data: dict):

    client_type = data["client_type"]
    budget = data["budget"]

    result = generate_proposal(client_type, budget)

    db = SessionLocal()

    proposal = Proposal(
        client_type=client_type,
        budget=budget,
        proposal_json=str(result)
    )

    db.add(proposal)
    db.commit()

    return result

@app.post("/generate-impact")
def impact_api(data: dict):

    product_name = data["product_name"]
    quantity = data["quantity"]

    result = generate_impact(product_name, quantity)

    return result
@app.post("/whatsapp-support")
def whatsapp_support(data: dict):

    message = data["message"]

    result = generate_whatsapp_reply(message)

    return result