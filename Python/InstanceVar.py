class InstanceVar:
    def __init__(self):
        self.text_list = []

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

    def sort(self, reverse = False):
        self.text_list.sort(reverse=reverse)


if __name__ == '__main__':
    pass