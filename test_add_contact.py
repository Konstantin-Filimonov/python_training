# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from conatct import Contact
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        self.login(driver, "admin", "secret")
        self.add_contact(driver, u"Константин", u"Филимонов", "suspiria", "sibady", "zaozerniya", "89043278923", "10",
                         "January", "2005", "filimonov.kostia28@gmail.com")
        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def add_contact(self, driver, first_name, last_name, nickname, organization, address, mobile, date, month, year,
                    email):
        self.init_contact_creation(driver)
        # fill contact form
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(u"%s" % first_name)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(u"%s" % last_name)
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(nickname)
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys(organization)
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys(address)
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(mobile)
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(email)
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(date)
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(month)
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").clear()
        driver.find_element(By.NAME, "byear").send_keys(year)
        driver.find_element(By.NAME, "new_group").click()
        # submit creation contact
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def init_contact_creation(self, driver):
        driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert  # исправлено на актуальный метод
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert  # исправлено на актуальный метод
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text

        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()