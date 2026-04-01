# use pydantic schemas for validation and serialization
from pydantic import BaseModel , EmailStr , Field 
from typing import Optional

class UserSignin(BaseModel):
    user_name : str = Field(min_length=3  , max_length=20)
    email : EmailStr
    password : str = Field(min_length=8)
    full_name : str = Field(min_length=2)
    phone_number : str = Optional[None]

