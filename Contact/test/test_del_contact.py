from Contact.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name=u"test"))
    app.contact.delete_first_contact()
