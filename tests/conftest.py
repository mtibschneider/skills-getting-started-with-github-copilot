import copy

from fastapi.testclient import TestClient

from src import app as app_module

ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


def _reset_activities() -> None:
    app_module.activities = copy.deepcopy(ORIGINAL_ACTIVITIES)


import pytest


@pytest.fixture(autouse=True)
def reset_activities_fixture():
    _reset_activities()
    yield
    _reset_activities()


@pytest.fixture
def client():
    return TestClient(app_module.app)
