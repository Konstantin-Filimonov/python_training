# -*- coding: utf-8 -*-
from Group.model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name ="adad", header ="adada", footer ="adada"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)