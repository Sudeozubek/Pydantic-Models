from pydantic import BaseModel, Field, EmailStr, field_validator

class User(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=18)
    email: EmailStr
    is_active: bool = True

    @field_validator("name")
    def name_cannot_be_empty(cls, value):
        if not value.strip():
            raise ValueError("name cannot be empty")
        return value

try: 
    user = User(name="sude", age=21, email="sude@mail.com")
    print(user)
except Exception as e:
    print("error:", e)

