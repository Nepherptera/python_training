from model.contact import Contact


def test_create_new_contact(app):
    app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name",
                               nickname="nickname", title="title", company="company", address="address",
                               home_phone_number="65653645425", mobile_number="4535436253",
                               work_phone_number="4354362353456", fax_number="6535265465465",
                               email="mail@mail.ru",
                               email2="mail2@mail.ru", email3="mail3@mail.ru",
                               homepage="http://localhost/addressbook/edit.php", bday="17", bmonth="October",
                               byear="1998",
                               aday="21", amonth="July", ayear="2008", address2="address", home="home",
                               notes="notes"))


def test_create_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="", address="",
                               home_phone_number="", mobile_number="",
                               work_phone_number="", fax_number="",
                               email="",
                               email2="", email3="",
                               homepage="", bday="-", bmonth="-",
                               byear="",
                               aday="-", amonth="-", ayear="", address2="", home="",
                               notes=""))
