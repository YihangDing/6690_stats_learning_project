with open('covtype.data') as f:
    lines = f.readlines()
    print('num of rows: {}'.format(len(lines)))
    first_line = lines[0].split(',')
    print('num of cols: {}'.format(len(first_line)))
