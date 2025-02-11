# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
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

        self.open_home_page(driver)

        self.login(driver)

        self.init_contact_creation(driver)

        self.add_contact(driver)

        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def add_contact(self, driver):
        # fill contact form
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(u"Константин")
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(u"Филимонов")
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys("suspiria")
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys("sibady")
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys("zaozerniya")
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys("89043278923")
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys("filimonov.kostia28@gmail.com")
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text("10")
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text("January")
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").clear()
        driver.find_element(By.NAME, "byear").send_keys("2005")
        driver.find_element(By.NAME, "new_group").click()
        # submit creation contact
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def init_contact_creation(self, driver):
        driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, driver):
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys("secret")
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

