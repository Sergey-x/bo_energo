import fastapi as fa
import pytest
from httpx import AsyncClient, Response
from schemas.task_1 import GetEquationSolutionResponseSchema


class TestEquation:
    @classmethod
    def get_url(cls) -> str:
        return "/roots/"

    @classmethod
    def make_params_dict(cls, a, b, c) -> dict:
        return {
            "a": a,
            "b": b,
            "c": c,
        }

    @pytest.mark.parametrize(
        "a,b,c,expected_status",
        (
                (None, None, None, fa.status.HTTP_400_BAD_REQUEST),
                (1, None, None, fa.status.HTTP_400_BAD_REQUEST),
                (None, 1, None, fa.status.HTTP_400_BAD_REQUEST),
                (None, None, 1, fa.status.HTTP_400_BAD_REQUEST),
                (None, 1, 1, fa.status.HTTP_400_BAD_REQUEST),
                (1, None, 1, fa.status.HTTP_400_BAD_REQUEST),
                (1, 1, None, fa.status.HTTP_400_BAD_REQUEST),
                (1, 1, "nan", fa.status.HTTP_400_BAD_REQUEST),  # inf, nan not allowed
                (1, 1, "some-text", fa.status.HTTP_400_BAD_REQUEST),
                (0, 1, 1, fa.status.HTTP_400_BAD_REQUEST),  # проверяем, что a != 0, иначе ZeroDivisionError
                (1, 4, 2, fa.status.HTTP_200_OK),
        )
    )
    async def test_equation_with_bad_params(
            self,
            async_client: AsyncClient,
            a: float | None,
            b: float | None,
            c: float | None,
            expected_status: int,
    ):
        """Запросы с неуказанными параметрами a, b или c."""
        response: Response = await async_client.get(url=self.get_url(), params=self.make_params_dict(a, b, c))
        assert response.status_code == expected_status

    async def test_equation_without_solutions(self, async_client: AsyncClient):
        """Запросы с параметрами a, b, c, при которых уравнение не имеет корней в действительных числах."""
        response: Response = await async_client.get(url=self.get_url(), params=self.make_params_dict(4, 1, 4))
        assert response.status_code == fa.status.HTTP_200_OK

        response_body = GetEquationSolutionResponseSchema.model_validate(response.json())
        assert response_body.x1 is None
        assert response_body.x2 is None

    @pytest.mark.parametrize(
        "a,b,c,expected_status",
        (
                (1, 12, 36, fa.status.HTTP_200_OK),
                (1, 4, 4, fa.status.HTTP_200_OK),
        )
    )
    async def test_equation_with_one_solution(
            self,
            async_client: AsyncClient,
            a: float | None,
            b: float | None,
            c: float | None,
            expected_status: int,
    ):
        """Запрос с параметрами a, b, c, при которых уравнение имеет один корень."""
        response: Response = await async_client.get(url=self.get_url(), params=self.make_params_dict(a, b, c))
        assert response.status_code == expected_status

        response_body = GetEquationSolutionResponseSchema.model_validate(response.json())
        assert response_body.x1 == response_body.x2
        assert response_body.x1 == (-b / (2 * a))

    @pytest.mark.parametrize(
        "a,b,c,expected_status",
        (
                (1, 12, 30, fa.status.HTTP_200_OK),
                (1, 4, 2, fa.status.HTTP_200_OK),
        )
    )
    async def test_equation_with_two_solutions(
            self,
            async_client: AsyncClient,
            a: float | None,
            b: float | None,
            c: float | None,
            expected_status: int,
    ):
        """Запрос с параметрами a, b, c, при которых уравнение имеет два корня."""
        response: Response = await async_client.get(url=self.get_url(), params=self.make_params_dict(a, b, c))
        assert response.status_code == expected_status

        response_body = GetEquationSolutionResponseSchema.model_validate(response.json())
        assert response_body.x1 != response_body.x2
