from enum import Enum


class Facing(Enum):
    n = 0
    e = 1
    s = 2
    w = 3

    def turn_right(self):
        return Facing((self.value + 1) % 4)

    def turn_left(self):
        return Facing((self.value - 1) % 4)


def calc_step(step, x=0, y=0, f=Facing.n):
    direction = step[0].lower()
    dist = int(step[1:].strip())
    if direction == 'r':
        new_dir = f.turn_right()
    elif direction == 'l':
        new_dir = f.turn_left()
    else:
        new_dir = f

    if new_dir == Facing.n:
        return x, y+dist, new_dir
    elif new_dir == Facing.e:
        return x+dist, y, new_dir
    elif new_dir == Facing.s:
        return x, y-dist, new_dir
    else:
        return x-dist, y, new_dir


def calc_seq_dist(seq):
    steps = seq.split(', ')
    x = 0
    y = 0
    f = Facing.n
    for step in steps:
        x, y, f = calc_step(step, x, y, f)
    return abs(x) + abs(y)


INPUT = 'R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5'
print(calc_seq_dist(INPUT))