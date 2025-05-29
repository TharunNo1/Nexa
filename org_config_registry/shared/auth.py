from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "nexa-super-secret"  # In production, move to env variable
ALGORITHM = "HS256"

security = HTTPBearer()

def create_org_token(org_id: str):
    to_encode = {"org_id": org_id}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        org_id: str = payload.get("org_id")
        if org_id is None:
            raise HTTPException(status_code=403, detail="Invalid token")
        return org_id
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
