from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, first_name, last_name, nickname, organization, address, mobile, date, month, year,
            email):
        driver = self.app.driver
        self.init_contact_creation()
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

    def delete_first_contact(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH, "// *[ @ id = 'content'] / form[2] / div[2] / input").click()


    def init_contact_creation(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

