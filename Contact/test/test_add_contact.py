# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

def test_add_contact(app):
    app.session.login(username="admin", password= "secret")
    app.contact.add(firstname=u"Константин", lastname=u"Филимонов", nickname="suspiria", company="sibady", home="zaozerniya", mobile="89043278923", bday="10",
                         bmonth="January", byear="2005", email="filimonov.kostia28@gmail.com")
    app.session.logout()

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