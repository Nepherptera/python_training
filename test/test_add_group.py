# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий в качестве параметра фикстуру
    app.session.login(username="admin", password='secret')  # Вспомогательные методы из отдельного класса Application
    app.group.create(Group(name="rte", header="ret", footer="hdgfgh"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
