def read_input(path):
    ''' Read input file at 'path' to a list of strings. '''
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def firstlastnumber(line):
    ''' Find sum of first and last digit in strin 'line'. '''
    digits = [str(d) for d in range(0,10)]
    number = ''
    for c in line:
        if c in digits:
            number += c
            break
    for c in line[::-1]:
        if c in digits:
            number += c
            break
    return int(number)

if __name__ == '__main__':
    data = read_input('input.txt')

    # Task 1
    tot = sum([firstlastnumber(line) for line in data])
    print(f'Task 1: {tot}')

    