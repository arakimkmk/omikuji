import random

def generate_amidakuji(height, width):
    """Generate an amidakuji ladder with the given height and width."""
    ladder = [[' ' for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if random.random() < 0.5:
                ladder[i][j] = '-'
    return ladder

def print_amidakuji(ladder):
    """Print the amidakuji ladder."""
    for row in ladder:
        print(''.join(row))