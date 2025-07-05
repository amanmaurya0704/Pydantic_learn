from pydantic import BaseModel
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active:bool = True
    addresses: Address
    created_at: datetime = datetime.now()
    tags: List[str] = []

user = User(
    id=1,
    name="Aman",
    email = "aman@gmail.com",
    created_at=datetime(2025,3,15,23,23),
    addresses=Address(
        street="something",
        city="Delhi",
        zip_code="201301"),
        is_active=False,
        tags = ["premium","subscriber"]
)


print(user)
