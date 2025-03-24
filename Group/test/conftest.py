# -*- coding: utf-8 -*-
from Group.fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")  # Получаем параметр браузера
    base_url = request.config.getoption("--baseUrl")

    # Проверяем, если fixture не инициализирована или её состояние невалидно
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)

    fixture.session.ensure_login("admin", "secret")  # Логинимся
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture  # Указываем, что будем изменять глобальную переменную

    def fin():
        if fixture is not None:  # Проверка на случай, если fixture = None
            fixture.session.ensure_logout()  # Логаут
            fixture.destroy()  # Разрушение объекта

    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
