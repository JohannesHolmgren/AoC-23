from itertools import product

def read_input(path):
    ''' Read input file at 'path' to a list of strings. '''
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def task1(data):
    ''' Get the sum of all numbers adjacent to a 
        symbol, excluding '.' and digits. '''
    # Iterate a row
    # If find a digit, save it in buffer
    # While digit:
    #   add to buffer
    #   if any around it not digit or dot:
    #       set flag "save" = true
    #   if flag is true:
    #       save to sum
    digits = [str(i) for i in range(10)]
    excluded = digits + ['.']
    print(excluded)
    numbersum = 0
    buffer = ''
    save = False

    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if not c in digits:
                if save == True and buffer != '':
                    numbersum += int(buffer)
                buffer = ''
                save = False
                continue
            buffer += c
            xrange = (max(0, x-1), min(len(row), x+2))
            yrange = (max(0, y-1), min(len(row), y+2))
            for pos in product(range(xrange[0], xrange[1]), range(yrange[0], yrange[1])):
                if data[pos[1]][pos[0]] not in excluded:
                    save = True
                    break
        if save == True and buffer != '':
            numbersum += int(buffer)
        buffer = ''
        save = False
        

    return numbersum

if __name__ == '__main__':
    data = read_input('input.txt')
    result1 = task1(data)
    print(f'Task 1: {result1}')