from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Contact.fixture.contact import ContactHelper
from Contact.fixture.session import SessionHelper
from Group.fixture.session import SessionHelper


class Application:

    def __init__(self):
        service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def setUp(self):
        service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def open_php_my_admin(self):
        self.driver.get("http://localhost/phpmyadmin/index.php?route=/sql&db=addressbook&table=addressbook&pos=0")

    def destroy(self):
        self.driver.quit()
