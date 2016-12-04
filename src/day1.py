from enum import Enum

from math import sqrt


class Facing(Enum):
    n = 0
    e = 1
    s = 2
    w = 3

    def turn_right(self):
        return Facing((self.value + 1) % 4)

    def turn_left(self):
        return Facing((self.value - 1) % 4)


def _direction(f, step):
    direction = step[0].lower()
    if direction == 'r':
        new_dir = f.turn_right()
    elif direction == 'l':
        new_dir = f.turn_left()
    else:
        new_dir = f
    return new_dir


def _distance(step):
    return int(step[1:].strip())


def calc_step(step, x=0, y=0, f=Facing.n):
    new_dir = _direction(f, step)
    dist = _distance(step)
    if new_dir == Facing.n:
        return x, y+dist, new_dir
    elif new_dir == Facing.e:
        return x+dist, y, new_dir
    elif new_dir == Facing.s:
        return x, y-dist, new_dir
    else:
        return x-dist, y, new_dir


def _split(seq):
    return seq.split(', ')


def _init():
    return 0, 0, Facing.n


def calc_seq_dist(seq):
    steps = _split(seq)
    x, y, f = _init()
    for step in steps:
        x, y, f = calc_step(step, x, y, f)
    return abs(x) + abs(y)


def _step_seq(x, y, dx, dy, steps):
    seq = []
    for i in range(steps):
        x = x + dx
        y = y + dy
        seq.append((x, y))
    return seq


def calc_seq_crossing(seq):
    steps = _split(seq)
    coord_hash = set()
    x, y, dir = _init()
    coord_hash.add((x, y))
    for step in steps:
        dir = _direction(dir, step)
        dist = _distance(step)
        if dir == Facing.n:
            seq = _step_seq(x, y, 0, 1, dist)
        elif dir == Facing.e:
            seq = _step_seq(x, y, 1, 0, dist)
        elif dir == Facing.s:
            seq = _step_seq(x, y, 0, -1, dist)
        else:
            seq = _step_seq(x, y, -1, 0, dist)
        for coord in seq:
            if coord in coord_hash:
                return coord
            else:
                coord_hash.add(coord)
                x, y = coord
    return None


INPUT = 'R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5'
print(calc_seq_dist(INPUT))
x, y = calc_seq_crossing(INPUT)
dist = abs(x) + abs(y)
print('answer %s, %s; distance %s' % (x, y, dist))