from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, nickname=None, organization=None, address=None, mobile=None, date=None, month=None, year=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.organization = organization
        self.address = address
        self.mobile = mobile
        self.date = date
        self.month = month
        self.year = year
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize