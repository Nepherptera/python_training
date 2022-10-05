from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "bday" or field_name == "bmonth" or field_name == "aday" or field_name == "amonth":
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # open home page
        self.app.open_home_page()
        # init edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def test_edit_contact_from_contact_page(self, contact):
        wd = self.app.wd
        # open home page
        self.app.open_home_page()
        self.open_contact_page()
        # init edit contact
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        wd.switch_to.alert.accept()

    def delete_contact_from_contact_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_page()
        # init edit contact
        wd.find_element_by_name("modifiy").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_link_text("home").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def assertRegexpMatches(self, param, param1):
        pass

    def close_alert_and_get_its_text(self):
        pass

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            cells = element.find_elements_by_tag_name("td")
            lastname = cells[1].text
            firstname = cells[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts

