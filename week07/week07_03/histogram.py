class Histogram:

    def __init__(self):
        self.histo_dict = {}

    def add(self, element, count):
        self.histo_dict[element] = count

    def count(self, element):
        if element not in self.histo_dict:
            return None
        return self.histo_dict[element]

    def get_dict(self):
        return self.histo_dict

    def items(self):
        return [(key, value) for key, value in self.histo_dict.items()]
