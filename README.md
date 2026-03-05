# AI Sustainable Marketplace Assistant

## Overview

The **AI Sustainable Marketplace Assistant** is a FastAPI-based backend system designed to help sustainable marketplaces automate product categorization, generate client proposals, and estimate environmental impact.

The system uses AI-based logic to:

* Automatically classify eco-friendly products
* Generate customized business proposals
* Calculate sustainability impact metrics

This project demonstrates how AI can assist **green marketplaces, eco-product sellers, and sustainability-focused businesses**.

---

# Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Uvicorn**
* **OpenAI / AI logic modules**

---

# Project Structure

```
app/
│
├── main.py
├── database.py
├── models.py
├── category_model.py
├── proposal_model.py
├── impact_model.py
│
└── __init__.py
```


---

# Module 1 – Product Category Generator

## Objective

Automatically classify a product into sustainability-related categories.

## Input

```
{
  "name": "Bamboo Toothbrush",
  "description": "Eco friendly biodegradable toothbrush made from bamboo"
}
```

## Process

The system analyzes:

* Product name
* Product description

It then generates:

* Primary Category
* Sub Category
* SEO Tags
* Sustainability Filters

## Example Output

```
{
 "primary_category": "Personal Care",
 "sub_category": "Eco Friendly Dental Products",
 "seo_tags": ["bamboo", "eco-friendly", "biodegradable"],
 "sustainability_filters": ["plastic-free", "biodegradable"]
}
```

## API Endpoint

```
POST /generate-category
```

---

# Module 2 – Proposal Generator

## Objective

Generate a **custom proposal for marketplace clients** based on their business type and budget.

## Input

```
{
  "client_type": "eco startup",
  "budget": 5000
}
```

## Process

The AI proposal generator creates a structured business proposal including:

* recommended product categories
* estimated marketing strategy
* suggested sustainability initiatives

## Example Output

```
{
 "proposal_title": "Sustainable Product Launch Strategy",
 "recommended_products": ["Bamboo Toothbrush", "Reusable Water Bottle"],
 "marketing_strategy": "Focus on eco conscious social media campaigns",
 "estimated_roi": "High potential in green consumer market"
}
```

## API Endpoint

```
POST /generate-proposal
```

---

# Module 3 – Environmental Impact Calculator

## Objective

Estimate the environmental impact of sustainable product purchases.

## Input

```
{
  "product_name": "Bamboo Toothbrush",
  "quantity": 100
}
```

## Process

The system calculates:

* Plastic saved
* Carbon emissions avoided
* Sustainability impact statement

## Example Output

```
{
 "plastic_saved": 2,
 "carbon_avoided": 12,
 "impact_statement": "This order contributes to reducing plastic waste and lowering carbon emissions."
}
```

## API Endpoint

```
POST /generate-impact
```

---

# Database

The system stores data using **SQLite + SQLAlchemy**.

### Tables

### Product Table

Stores product category results.

Fields:

* id
* name
* description
* category
* sub_category
* tags
* filters

### Proposal Table

Stores generated client proposals.

Fields:

* id
* client_type
* budget
* proposal_json

---

# Running the Project

## Step 1 – Install Dependencies

```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
```

---

## Step 2 – Start the Server

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides Swagger documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

From here you can test all APIs.

Available APIs:

* `/generate-category`
* `/generate-proposal`
* `/generate-impact`

---

# Example API Request

## Generate Category

```
curl -X POST http://127.0.0.1:8000/generate-category \
-H "Content-Type: application/json" \
-d '{
"name": "Bamboo Toothbrush",
"description": "Eco friendly biodegradable toothbrush made from bamboo"
}'
```

---

# Future Improvements

* Integrate real **OpenAI GPT models**
* Add **carbon footprint datasets**
* Build **frontend dashboard**
* Support **multiple sustainable product types**
* Deploy using **Docker + Cloud**

---

# Author

Project developed as part of an **AI Backend Development Task using FastAPI**.

https://github.com/user-attachments/assets/93872dea-b5f7-4dc3-9b4a-aca83cb30c67
