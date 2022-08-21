# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # инициализация, создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указание на то, как эта фикстура должна быть разрушена
    return fixture


def test_add_group(app):  # Тестовый метод, принимающий в качестве параметра фикстуру
    app.session.login(username="admin", password='secret')  # Вспомогательные методы из отдельного класса Application
    app.group.create(Group(name="rte", header="ret", footer="hdgfgh"))
    app.session.logout()


def test_empty_add_group(app):
    app.session.login(username="admin", password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
