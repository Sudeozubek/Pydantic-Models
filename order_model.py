from pydantic import BaseModel, Field, field_validator

class Order(BaseModel):
    order_id: int = Field(..., gt=0)
    customer_name: str = Field(..., min_length=3)
    items : list[str]
    total_price: float = Field(..., gt=0)
    status: str

    @field_validator("items")
    def check_items_not_empty(cls, value): 
        if not value:
            raise ValueError("siparis en az 1 ürün içermelidir!")
        return value

    @field_validator("status")
    def allowed_statuses(cls, value):
        allowed_statuses = {"pending", "shipped", "delivered"}
        if value not in allowed_statuses:
            raise ValueError(f"status must be one of {allowed_statuses}")
        return value
try:
    order = Order(order_id=2, customer_name="Sude", items=["Laptop"], total_price=1500, status="shipped")
    print("successful ordered", order)
except Exception as e:
    print("error:", e) 
