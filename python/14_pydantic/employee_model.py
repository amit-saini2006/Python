from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee Name',
        examples='Amit Saini'
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000,
        le=3000000,
        description='Annual salary in USD'
    )

from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        description="Valid email address"
    )
    phone: str = Field(
        ...,
        regex=r'^\+?[1-9]\d{9,14}$',
        description="Phone number with optional country code"
    )
    age: int = Field(
        ...,
        ge=0,
        le= 100,
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount in percentage"
    )

# Email regex:
# ^[a-zA-Z0-9._%+-]+ → allows letters, digits, and some symbols before @
# @[a-zA-Z0-9.-]+ → allows domain names
# \.[a-zA-Z]{2,}$ → requires a top-level domain like .com, .in, .org, etc.

# Phone regex:
# ^\+? → optional + at the start
# [1-9]\d{9,14}$ → ensures 10–15 digits (no leading zero)
