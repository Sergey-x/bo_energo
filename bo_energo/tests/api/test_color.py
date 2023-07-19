import fastapi as fa
import pytest
from enums.color import ColorEnum
from httpx import AsyncClient, Response
from schemas.task_2 import MAX_NUMBER, MIN_NUMBER, GetColorResponseSchema


class TestColor:
    @classmethod
    def get_url(cls) -> str:
        return "/color/"

    @pytest.mark.parametrize(
        "n,expected_status",
        (
                (MIN_NUMBER - 1, fa.status.HTTP_400_BAD_REQUEST),
                (MAX_NUMBER + 1, fa.status.HTTP_400_BAD_REQUEST),
        )
    )
    async def test_color_with_various_params(
            self,
            async_client: AsyncClient,
            n,
            expected_status: int,
    ):
        response: Response = await async_client.get(url=self.get_url(), params={"number": n})
        assert response.status_code == expected_status

    async def test_color_with_good_params(
            self,
            async_client: AsyncClient,
    ):
        response: Response = await async_client.get(url=self.get_url(), params={"number": MAX_NUMBER})
        assert response.status_code == fa.status.HTTP_200_OK
        response_body = GetColorResponseSchema.model_validate(response.json())
        assert response_body.color == ColorEnum.BLUE
