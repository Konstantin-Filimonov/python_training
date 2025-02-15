# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.open_groupe_page(driver)
        self.create_group(driver, Group(name = "adad", header = "adada", footer = "adada"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.open_groupe_page(driver)
        self.create_group(driver, Group("", "", ""))
        self.return_to_groups_page(driver)
        self.logout(driver)



    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, driver, group):
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()

    def open_groupe_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, driver, username, password):
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()