from pydantic import BaseModel, Field, field_validator

class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    in_stock: bool = True
    category: str

    @field_validator("category")
    def check_category(cls, value):
        allowed_categories={"electronics", "clothing", "food"}
        if value not in allowed_categories:
            raise ValueError(f"Invalid category! Just {allowed_categories}")
        return value

try:
    product = Product(name="Laptop", price=1200, category="electronics")
    print(product)
except Exception as e:
    print("error:", e)

try:
    product = Product(name="Apple", price=3.22, category="food")
    print(product)
except Exception as e:
    print("error:", e)

