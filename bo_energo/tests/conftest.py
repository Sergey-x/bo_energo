import asyncio
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from requests import Session as RequestSession
from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def event_loop():
    """
    Creates event loop for tests.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client(app: FastAPI, client: TestClient) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url=client.base_url) as async_test_client:
        yield async_test_client


@pytest.fixture
def client(app: FastAPI) -> Generator[RequestSession, None, None]:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def app() -> FastAPI:
    from main import app as fastapi_app

    return fastapi_app
