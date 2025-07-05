from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_activate:bool

input_data = {'id':'101','name':"Aman",'is_activate':0}
user = User(**input_data)
print(user)


