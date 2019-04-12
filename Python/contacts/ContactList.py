class ContactList:
    def __init__(self):
        self.contact_list = []
        

    def add(self, ci):
        self.contact_list.append(ci)

    def find(self, name):
       return [ci for ci in self.contact_list  if ci.name == name]

    def getList(self, start=0, end=None):
        return self.contact_list[start:end]

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if(self.current < len(self.contact_list)):
            current = self.current
            self.current += 1
            return self.contact_list[current]

        raise StopIteration()