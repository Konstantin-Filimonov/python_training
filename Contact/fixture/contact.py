from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ..model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        driver = self.app.driver
        self.init_contact_creation()
        self.fill_contact_form(contact)
        # submit creation contact
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def return_to_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home").click()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        driver.find_element(By.XPATH, "// *[ @ id = 'content'] / form[2] / div[2] / input").click()
        self.contact_cache = None

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        # open modification form
        driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element(By.NAME, "update").click()
        self.return_to_contact_page()
        self.contact_cache = None


    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        # open modification form
        driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element(By.NAME, "update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def init_contact_creation(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contact_page()
            self.contact_cache = []
            for row in driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(
                        first_name=first_name,
                        last_name=last_name,
                        id=id,
                        all_phones_from_home_page=all_phones
                    )
                )
        return list(self.contact_cache)

    def open_home_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/")):
            driver.find_element(By.LINK_TEXT, "home").click()

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = driver.find_element(By.NAME, "home").get_attribute("value")
        mobile = driver.find_element(By.NAME, "mobile").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, homephone = homephone, mobile=mobile)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        return Contact(homephone = homephone, mobile=mobile)
