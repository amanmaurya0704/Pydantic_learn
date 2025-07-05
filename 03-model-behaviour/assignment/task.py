from pydantic import BaseModel,Field,computed_field,model_validator,field_validator

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int = Field(...,ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_night
    

input ={'user_id':101,'room_id':1001,'nights':0,'rate_per_night':100}
booking = Booking(**input)
print(booking)

    
