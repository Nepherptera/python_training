from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="1", middlename="1", lastname="1",
                                           nickname="1", title="1", company="1", address="1",
                                           home_phone_number="1", mobile_number="1",
                                           work_phone_number="1", fax_number="1",
                                           email="1",
                                           email2="1", email3="1",
                                           homepage="1", bday="25", bmonth="January",
                                           byear="2002",
                                           aday="21", amonth="September", ayear="2003", address2="1", home="1",
                                           notes="1"))
    app.session.logout()


def test_edit_contact_from_contact_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_edit_contact_from_contact_page(Contact(firstname="2", middlename="2", lastname="2",
                                                            nickname="2", title="2", company="2", address="2",
                                                            home_phone_number="2", mobile_number="2",
                                                            work_phone_number="2", fax_number="2",
                                                            email="2",
                                                            email2="2", email3="2",
                                                            homepage="2", bday="28", bmonth="March",
                                                            byear="2007",
                                                            aday="17", amonth="June", ayear="2005", address2="2",
                                                            home="2",
                                                            notes="2"))
    app.session.logout()
