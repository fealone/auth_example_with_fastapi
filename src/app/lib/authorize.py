import json

from app.settings import JWKS

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader

import jwt


router = APIRouter()

api_key = APIKeyHeader(name="Authorization", auto_error=False)


async def authorize_user(
        authorization: str = Depends(api_key)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate token",
        headers={"WWW-Authenticate": authorization},
    )
    if authorization:
        auth = authorization.split(" ")
    if len(auth) != 2:
        raise credentials_exception
    if auth[0] != "Bearer":
        raise credentials_exception
    id_token = auth[1]
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(JWKS["keys"][0]))
    try:
        payload = jwt.decode(
                id_token,
                public_key,
                algorituhms=JWKS["keys"][0]["alg"])
    except Exception:
        raise credentials_exception
    return {"user": payload["user"], "email": payload["email"]}
