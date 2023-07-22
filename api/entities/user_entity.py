class UserEntity:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password