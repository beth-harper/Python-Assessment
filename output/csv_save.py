
def csv_save(data, postcode, start_date, end_date):

    '''

    Writes the filtered list of crimes to csv.
    Optional for user user to save/not save

    '''

    filename = postcode + '_from_' + start_date + '_to_' + end_date + '.csv'

    new_file = open(filename, 'w')

    for row in data:
        temp_row = ''
        for element in row:  # cleaning quotes and brackets
            element.lstrip('\'')
            element.lstrip('[')
            element.lstrip(']')
            if element == '\n':
                continue
            temp_row = temp_row + element + ','  # recreates csv file
        row = temp_row + '\n'
        new_file.write('%s' % row)

    new_file.close()


if __name__ == '__main__':

    print('testing csv_save.py')  # Unit Testing

    print('All tests have run successfully!')
