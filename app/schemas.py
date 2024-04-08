from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str

class ResponseUserSchema(BaseModel):
    email: EmailStr
    id: int

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class PostBaseSchema(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreateSchema(PostBaseSchema):
    pass

class ResponsePostSchema(PostBaseSchema):
    id: int
    created_at: datetime
    owner_id: int
    owner: ResponseUserSchema

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    id: Optional[int] = None