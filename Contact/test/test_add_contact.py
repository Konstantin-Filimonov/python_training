# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from Contact.model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(Contact(first_name=u"Константин", last_name=u"Филимонов", nickname="suspiria", organization="sibady", address="zaozerniya", mobile="89043278923", date="10",
                         month="January", year="2005", email="filimonov.kostia28@gmail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True

def is_alert_present(self):
    try:
        self.app.driver.switch_to.alert  # исправлено на актуальный метод
    except NoAlertPresentException:
        return False
    return True

def close_alert_and_get_its_text(self):
    try:
        alert = self.app.driver.switch_to.alert  # исправлено на актуальный метод
        alert_text = alert.text
        if self.app.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    finally: self.accept_next_alert = True