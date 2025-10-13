from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 101, 'name': "Amit", 'is_active': True}

user = User(**input_data)
print(user)

# import baseModel
# type annotations
# Model init (Always upack the dict)
# Automatic Validation