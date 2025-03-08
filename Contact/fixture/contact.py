from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        driver = self.app.driver
        self.init_contact_creation()
        self.fill_contact_form(contact)
        # submit creation contact
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.organization)
        self.change_field_value("home", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("bday", contact.date)
        self.change_field_value("bmonth", contact.month)
        self.change_field_value("byear", contact.year)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(u"%s" % text)

    def delete_first_contact(self):
        driver = self.app.driver
        self.select_first_contact()
        driver.find_element(By.XPATH, "// *[ @ id = 'content'] / form[2] / div[2] / input").click()

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        # open modification form
        driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element(By.NAME, "update").click()

    def init_contact_creation(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

