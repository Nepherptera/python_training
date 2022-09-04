# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий в качестве параметра фикстуру
    app.group.create(Group(name="rte", header="ret", footer="hdgfgh"))
    app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
