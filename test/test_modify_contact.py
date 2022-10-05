from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="1", lastname="1",
                      nickname="1", title="1", company="1", address="1",
                      home="1", mobile="1",
                      work="1", fax="1",
                      email="1",
                      email2="1", email3="1",
                      homepage="1", bday="25", bmonth="January",
                      byear="2002",
                      aday="21", amonth="September", ayear="2003", address2="1", phone2="1",
                      notes="1")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_contact_from_contact_page(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact())
#    app.contact.test_edit_contact_from_contact_page(Contact(firstname="2", middlename="2", lastname="2",
#                                                            nickname="2", title="2", company="2", address="2",
#                                                            home="2", mobile="2",
#                                                            work="2", fax="2",
#                                                            email="2",
#                                                            email2="2", email3="2",
#                                                            homepage="2", bday="28", bmonth="March",
#                                                            byear="2007",
#                                                            aday="17", amonth="June", ayear="2005", address2="2",
#                                                            phone2="2",
#                                                            notes="2"))
