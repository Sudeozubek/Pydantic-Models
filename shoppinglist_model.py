from pydantic import BaseModel, Field, field_validator

class ShoppingList(BaseModel):
    item_name: str = Field(...)
    amount: float  = Field(..., ge=1)
    is_purchased: bool = False

    @field_validator("item_name") 
    def check_empty_item_name(cls, value):
      if not value.strip():
          raise ValueError("item_name cannot be empty")
      return value

try:
    shopping_list = ShoppingList(item_name="Ayakkabı", amount=55.4)
    print(shopping_list)
except Exception as e:
    print(e)
