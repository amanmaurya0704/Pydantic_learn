from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street:str
    city: str
    postalcode:str

class User(BaseModel):
    id:int
    name:str
    address: Address

class Comment(BaseModel):
    id :int
    content:str
    replies:Optional[List['Comment']]= None

Comment.model_rebuild()


address = Address(
    street = "6D",
    city = "Noida",
    postalcode="201301"
)

user = User(
    id=101,
    name="Aman Maurya",
    address=address
)

comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2,content="reply1"),
        Comment(id=3,content="reply2")
    ]
)

print(user)
print(comment)