
class ColumnChart(object):
    max_height_point = 3

    def __init__(self, data):
        self.data = data
        self.highest_value = self.find_max_value()
        print(data)
        print(self.highest_value)

    def create_columns(self):
        pass

    def find_max_value(self):
        max_value = 0
        for row in self.data:
            if row[1] > max_value:
                max_value = row[1]

        return max_value

class Column(object):
    def __init__():
        pass
