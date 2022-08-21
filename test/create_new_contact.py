import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_contact(app):
    app.session.login(username="admin", password="secret")
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
    app.session.logout()
