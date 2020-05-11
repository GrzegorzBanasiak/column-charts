

def get_data_from(data_path):
    data = []

    try:
        with open(data_path, 'r') as file:
            for line in file:
                line_rstrip = line.rstrip()     # remove /n
                line_split = line_rstrip.split(';')

                data.append([ line_split[0], float(line_split[1]) ])

        return data
    except IOError:
        print('Not found file: ' + data_path + '. The process has been aborted!')
        raise
