import statistics
from cmath import sqrt


class MyData:
    name = ''
    path = ''
    data = []
    values = []
    mean = 0
    variance = 0
    stdev = 0

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.get_data()
        self.values = [float(x) for x in self.values]
        self.mean = statistics.mean(self.values)
        self.variance = statistics.variance(self.values)
        self.stdev = statistics.stdev(self.values)

    def get_values(self):
        very_strange_python_list_logic = []
        for line in self.data:
            if line != '\n':
                very_strange_python_list_logic.append(line.split()[-1])
        self.values = very_strange_python_list_logic

    def get_data(self):
        with open(self.path) as f:
            f = f.readlines()
        self.data = f
        self.get_values()

    def get_t_test(self, comparable_data):
        return (self.mean - comparable_data.mean) / sqrt(
            pow(self.stdev, 2) / len(self.values) + pow(comparable_data.stdev, 2) / len(comparable_data.values))

    def get_f_test(self, comparable_data):
        return self.variance / comparable_data.variance
