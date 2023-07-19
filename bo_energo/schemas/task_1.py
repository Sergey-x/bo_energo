import pydantic as pd


class GetDiscriminantResponseSchema(pd.BaseModel):
    x1: None | float
    x2: None | float
