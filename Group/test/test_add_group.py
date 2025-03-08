# -*- coding: utf-8 -*-
from Group.model.group import Group

def test_add_group(app):
    app.group.create(Group(name ="adad", header ="adada", footer ="adada"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

