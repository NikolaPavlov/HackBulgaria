class Histogram:

    def __init__(self):
        self.__histogram = {}

    def add_item_to_histogram(self, item):
        if item in self.__histogram:
            self.__histogram[item] += 1
        else:
            self.__histogram[item] = 1

    def add_to_histogram_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                if 'Apache' in line:
                    self.add_item_to_histogram('Apache')
                elif 'nginx' in line:
                    self.add_item_to_histogram('nginx')
                elif 'Microsoft' in line:
                    self.add_item_to_histogram('Microsoft IIS')
                elif 'IBM' in line:
                    self.add_item_to_histogram('IBM Http Server ')

    def get_dict(self):
        return(self.__histogram)

