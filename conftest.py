import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:  # Если фикстуры нет
        fixture = Application()  # Инициализируем фикстуру
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password='secret')  # логин в одной сессии
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
