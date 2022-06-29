import pytest


@pytest.fixture(params=["first","second",("third","3th")])
def dataload(request ):
    print("data of param will print")
    return request.param