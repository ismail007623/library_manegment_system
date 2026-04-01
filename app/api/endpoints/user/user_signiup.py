from fastapi import APIRouter
from app.schemas.user_schema import UserSignin

app = APIRouter ()

@app.post('/sign-in')
async def sign_in(user: UserSignin):
    """
    """
    try:
        user_name = user.user_name
        email = user.email
        password = user.password
        full_name = user.full_name
        phone_number = user.phone_number
        ismail = 89

        

