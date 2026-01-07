from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    # This matches the 'sub' (subject) field in the JWT
    user_id: Optional[UUID] = None