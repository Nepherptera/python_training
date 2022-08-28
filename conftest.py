import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()  # инициализация, создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указание на то, как эта фикстура должна быть разрушена
    return fixture
