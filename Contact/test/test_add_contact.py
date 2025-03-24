# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from Contact.model.contact import Contact
from sys import maxsize


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name=u"Константин",
        last_name=u"Филимонов",
        homephone="+14124124",
        mobile="89043278923"
    )

    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    contact.id = new_contacts[-1].id  # Назначаем ID последнего добавленного контакта

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
