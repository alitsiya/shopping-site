"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self,
         first_name,
         last_name,
         email,
         password,
         ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):
        return "<User: %s, %s, %s>" % (self.first_name, self.last_name, self.email)


def read_user_data_from_file(filepath):
    # """Read melon type data and populate dictionary of melon types.

    # Dictionary will be {email: Customer object}
    # """

    customer_data = {}

    for line in open(filepath):
        first_name, last_name, email, password = line.strip().split("|")

        customer_data[email] = Customer(first_name, last_name, email, password)

    return customer_data


def get_by_email(email):
    # """Return a customer, given his/her email."""
    return customer_data[email]


customer_data = read_user_data_from_file("customers.txt")