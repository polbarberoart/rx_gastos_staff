import reflex as rx
from typing import List, Optional
from sqlmodel import Field, Relationship

class Category(rx.Model, table=True):
    """Catálogo oficial de tipos de gastos."""
    
    name: str = Field(unique=True, nullable=False, index=True)
    description: Optional[str] = Field(default=None)
    
    # RELACIÓN:
    # Una categoría puede estar presente en muchos gastos.
    expenses: List["Expense"] = Relationship(back_populates="category_ref")