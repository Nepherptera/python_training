from model.contact import Contact

# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def random_num(prefix, maxlen):
    numbers = string.digits
    return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home="", mobile="", work="", fax="", email="", email2="", email3="",
                    homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                    ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 20),
                       nickname=random_string("nickname", 20), title=random_string("title", 20),
                       company=random_string("company", 20), address=random_string("address", 20),
                       home=random_num("", 10), mobile=random_num("", 10), work=random_num("", 10),
                       fax=random_num("", 10),
                       email=random_string("email", 20), email2=random_string("email2", 20),
                       email3=random_string("email3", 20),
                       homepage=random_string("homepag", 10), bday="12", bmonth=random.choice(months),
                       byear="1994",
                       aday="16", amonth=random.choice(months), ayear="2008",
                       address2=random_string("address2", 10), phone2=random_num("", 10),
                       notes=random_string("notes", 15)) for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_new_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

