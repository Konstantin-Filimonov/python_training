from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ..model.contact import Contact


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
        self.change_field_value("company", contact.organization)
        self.change_field_value("home", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

        select = Select(driver.find_element(By.NAME, "bday"))
        select.select_by_visible_text("10")

        select = Select(driver.find_element(By.NAME, "bmonth"))
        select.select_by_visible_text("January")

        self.change_field_value("byear", contact.year)

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
            self.contact_cache = []  # Инициализируем contact_cache как пустой список
            driver = self.app.driver
            self.open_contact_page()
            for element in driver.find_elements(By.CSS_SELECTOR, "[name=entry]"):
                first_name = element.find_element(By.XPATH, ".//td[3]").text
                last_name = element.find_element(By.XPATH, ".//td[2]").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.contact_cache)
