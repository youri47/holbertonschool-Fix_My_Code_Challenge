#!/usr/bin/python3
""" User module """
from hashlib import md5


class User:
    """ User class """

    def __init__(self, name, password):
        self.id = None
        self.name = name
        self.password = password

    @property
    def password(self):
        """ password getter """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ encrypts password with md5 before storing """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """ checks password validity """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        return md5(pwd.encode()).hexdigest().lower() == self.password


if __name__ == "__main__":
    print("Test User")
    u = User("John", "Holberton")
    if u.is_valid_password("Holberton") is False:
        print("is_valid_password should return True if it's the right password")
