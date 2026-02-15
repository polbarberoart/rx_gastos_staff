import reflex as rx
from typing import List, Optional
from sqlmodel import Field, Relationship

class Staff(rx.Model, table=True):
    name: str = Field(nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    
    # Guardamos el hash, no la contraseña plana
    password_hash: str = Field(nullable=False)
    
    role: str = Field(default="staff") # admin, staff, viewer
    
    # Relación con los gastos
    expenses: List["Expense"] = Relationship(back_populates="staff_ref")