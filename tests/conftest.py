import pytest
from rest.lambdatest import LambdatestService


@pytest.fixture
def context():
    return dict()


@pytest.fixture(scope="session")
def lambdatest_service():
    return LambdatestService()
