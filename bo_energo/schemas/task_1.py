import pydantic as pd


class GetEquationSolutionRequestSchema(pd.BaseModel):
    """Параметры квадратичного уравнения."""
    a: pd.confloat(allow_inf_nan=False)
    b: pd.confloat(allow_inf_nan=False)
    c: pd.confloat(allow_inf_nan=False)

    @pd.field_validator("a")
    def a_must_be_not_equal_0(cls, a):
        """Если `a` равно 0, то уравнение не квадратное."""
        if a == 0:
            raise ValueError("Incorrect argument: `a`.")
        return a


class GetEquationSolutionResponseSchema(pd.BaseModel):
    x1: None | float
    x2: None | float
