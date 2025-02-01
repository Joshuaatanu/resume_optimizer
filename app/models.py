from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserDB(UserBase):
    id: str
    disabled: bool = False
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ResumeUpload(BaseModel):
    description: Optional[str] = None

class JobDescriptionUpload(BaseModel):
    job_title: Optional[str] = None

class GeneratedDocument(BaseModel):
    user_id: str
    document_type: str
    content: str
    version: int
