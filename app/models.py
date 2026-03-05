from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    category = Column(String)
    sub_category = Column(String)
    tags = Column(Text)
    filters = Column(Text)


class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True)
    client_type = Column(String)
    budget = Column(Integer)
    proposal_json = Column(Text)