from functools import reduce

def read_input(path):
    ''' Read input file at 'path' to a list of strings. '''
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def get_possible_games(data):
    ''' Get sum of indices of all possible games '''
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    id_sum = 0
    for id, game in enumerate(data):
        # Get sets of cubes
        all_sets = game.split(':')[1]
        # Get separate sets
        sets = all_sets.split(';')
        is_ok = True
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                [amount, color] = cube.strip().split(' ')
                if int(amount) > max_cubes[color]:
                    is_ok = False
            if not is_ok:
                break
        else:
            id_sum += id+1
    return id_sum
                    
def get_fewest(data):
    ''' Get the sum of product of fewest number of cubes needed. '''
    power_sum = 0
    for id, game in enumerate(data):
        min_cubes = {'red': 0, 'green': 0,'blue': 0}
        # Get sets of cubes
        all_sets = game.split(':')[1]
        # Get separate sets
        sets = all_sets.split(';')
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                [amount, color] = cube.strip().split(' ')
                min_cubes[color] = max(int(amount), min_cubes[color])
        power_sum += reduce(lambda x, y: x*y, min_cubes.values())
    return power_sum


if __name__ == '__main__':
    # Read input
    data = read_input('input.txt')

    # Task 1
    result1 = get_possible_games(data)
    print(f'Task 1: {result1}')
    # Task 2
    result2 = get_fewest(data)
    print(f'Task 2: {result2}')