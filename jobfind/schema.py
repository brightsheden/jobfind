from pydantic import BaseModel, Field


class WaitListSchema(BaseModel):
    name: str = Field(..., title="Name", description="Name of the person on the waitlist")
    email: str = Field(..., title="Email", description="Email of the person on the waitlist")
  