import pytest
from Contact.fixture.applicationcont import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
