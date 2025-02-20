from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class BlogPost(BaseModel):
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=3)
    created_at: datetime = Field(default_factory=datetime.now)
    is_published: bool = False

    @field_validator("title", "content", "author")
    def check_not_empty(cls, value):
        if not value.strip():
            raise ValueError('title cannot be empty')
        return value

try:
    blogpost = BlogPost(title="My Blog", content="This is my blog post", author="Sude")
    print(blogpost)
except Exception as e:
    print(e)
