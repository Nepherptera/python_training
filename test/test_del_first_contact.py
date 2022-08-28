def test_delete_first_contact(app):
    app.session.login(username="admin", password='secret')
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact_from_contact_page(app):
    app.session.login(username="admin", password='secret')
    app.contact.delete_contact_from_contact_page()
    app.session.logout()
