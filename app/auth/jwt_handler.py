import time 
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Function returns the generated token
def token_response(token:str):
    return{
        "access_token":token
    }

# Generate the signIn token
def signJWT(userId:str):
    payload={
        "userID":userId,
        "expiry":time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)

# Decode the token
def decodeToken(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET,algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return{}