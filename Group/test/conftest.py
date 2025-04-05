# -*- coding: utf-8 -*-
from Group.fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target

    # Получаем параметры из командной строки
    browser = request.config.getoption("--browser")
    target_file = request.config.getoption("--target")

    # Загружаем конфигурацию
    if target is None:
        try:
            # Используем абсолютный путь к target.json
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), target_file)
            with open(config_path) as f:
                target = json.load(f)
        except FileNotFoundError:
            # Значения по умолчанию, если файл не найден
            target = {
                'baseUrl': 'http://localhost/addressbook/',
                'username': 'admin',
                'password': 'secret'
            }

    # Инициализация приложения
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])

    # Авторизация
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # Добавляем проверку на существование fixture
        if fixture is not None:
            try:
                fixture.session.ensure_logout()
            except AttributeError:
                pass  # Если session не существует
            try:
                fixture.destroy()
            except AttributeError:
                pass  # Если destroy не существует

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use: chrome or firefox")
    parser.addoption("--target", action="store", default="target.json",
                     help="Path to config file")