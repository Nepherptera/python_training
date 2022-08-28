def test_delete_first_group(app):
    app.session.login(username="admin", password='secret')  # Вспомогательные методы из отдельного класса Application
    app.group.delete_first_group()
    app.session.logout()