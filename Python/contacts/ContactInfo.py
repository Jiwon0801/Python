class ContactInfo:
    def __init__(self, name,email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))


if __name__ == '__main__':
    pass