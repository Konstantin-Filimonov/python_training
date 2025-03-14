from Contact.model.contact import Contact


def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name ="blabla"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(nickname ="suspir"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)