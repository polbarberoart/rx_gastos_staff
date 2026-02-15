import reflex as rx
from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship

# Importamos para que Python reconozca los tipos en las referencias
from .staff import Staff
from .category import Category

class Expense(rx.Model, table=True):
    """Tabla de Hechos: Registro de cada gasto individual."""
    concept: str = Field(nullable=False)
    amount: float = Field(default=0.0)
    date: datetime = Field(default_factory=datetime.now, index=True)
    
    # Llaves foráneas (Vínculo físico en DB)
    staff_id: int = Field(foreign_key="staff.id", index=True)
    category_id: int = Field(foreign_key="category.id", index=True)

    # Referencias de Python (Atajos para el código)
    staff_ref: Optional[Staff] = Relationship(back_populates="expenses")
    category_ref: Optional[Category] = Relationship(back_populates="expenses")