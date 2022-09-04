from model.contact import Contact


def test_create_new_contact(app):
    app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name",
                               nickname="nickname", title="title", company="company", address="address",
                               home="65653645425", mobile="4535436253",
                               work="4354362353456", fax="6535265465465",
                               email="mail@mail.ru",
                               email2="mail2@mail.ru", email3="mail3@mail.ru",
                               homepage="http://localhost/addressbook/edit.php", bday="17", bmonth="October",
                               byear="1998",
                               aday="21", amonth="July", ayear="2008", address2="address", phone2="325324",
                               notes="notes"))


def test_create_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="", address="",
                               home="", mobile="",
                               work="", fax="",
                               email="",
                               email2="", email3="",
                               homepage="", bday="-", bmonth="-",
                               byear="",
                               aday="-", amonth="-", ayear="", address2="", phone2="",
                               notes=""))
