
max_height_point = 3
max_scene_width = 6

class ColumnChart(object):

    def __init__(self, data):
        self.highest_value = self.find_max_value(data)
        self.columns = self.create_columns(data)
        print(data)
        print(self.highest_value)
        print(self.columns[3].hight)

    def create_columns(self, data):
        columns = []
        for row in data:
            column = Column(text = row[0], value = row[1])
            column.calculate_height(self.highest_value)
            columns.append(column)

        return columns

    def find_max_value(self, data):
        max_value = 0
        for row in data:
            if row[1] > max_value:
                max_value = row[1]

        return max_value

class Column(object):
    def __init__(self, text, value):
        self.text = text
        self.value = value

    def calculate_height(self, highest_value):
        self.hight = (self.value * max_height_point) / highest_value
