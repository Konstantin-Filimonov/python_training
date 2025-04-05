# -*- coding: utf-8 -*-
from Group.fixture.application import Application
import pytest
import json


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")  # Получаем параметр браузера
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    # Проверяем, если fixture не инициализирована или её состояние невалидно
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])  # Логинимся
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()  # Логаут
        fixture.destroy()  # Разрушение объекта
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--target", action="store", default="target.json")
