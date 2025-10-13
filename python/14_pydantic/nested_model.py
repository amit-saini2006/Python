from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street='123 xyz',
    city='delhi',
    postal_code='101010'
)

user = User(
    id=1,
    name='Amit Saini',
    address= address
)
print(user)