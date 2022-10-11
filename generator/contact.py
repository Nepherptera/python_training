from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                       notes=random_string("notes", 15)) for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
