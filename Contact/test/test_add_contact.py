# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

def test_untitled_test_case(app):
    app.session.login("admin", "secret")
    app.contact.add(u"Константин", u"Филимонов", "suspiria", "sibady", "zaozerniya", "89043278923", "10",
                         "January", "2005", "filimonov.kostia28@gmail.com")
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