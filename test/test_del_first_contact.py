from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.delete_first_contact()


def test_delete_contact_from_contact_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.delete_contact_from_contact_page()
