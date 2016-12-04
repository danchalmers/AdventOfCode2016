
default_keypad = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]


pt2_keypad = [[None, None, 1, None, None],
              [None, 2,3,4, None],
              [5,6,7,8,9],
              [None, 'A','B','C',None],
              [None, None, 'D', None, None]]


def _limit_keypad_size(x, y, keypad):
    x_, y_ = (max(0, min(x, len(keypad[0])-1)),
                max(0, min(y, len(keypad)-1))
            )
    if keypad[y_][x_]:
        return x_, y_
    else:
        return None


def _get_coord(step, x, y, keypad):
    if step == 'U':
        coord = _limit_keypad_size(x, y-1, keypad)
    elif step == 'D':
        coord = _limit_keypad_size(x, y+1, keypad)
    elif step == 'R':
        coord = _limit_keypad_size(x+1, y, keypad)
    else:
        coord = _limit_keypad_size(x-1, y, keypad)
    if coord:
        return coord
    else:
        return x, y


def _get_digit(line, x=1, y=1, keypad=default_keypad):
    for step in line:
        x, y = _get_coord(step.upper(), x, y, keypad)
    return keypad[y][x]


def get_digit(line, start=5, keypad=default_keypad):
    for y, row in enumerate(keypad):
        for x, val in enumerate(row):
            if val == start:
                return _get_digit(line, x, y, keypad)


def get_digits(rows, keypad=default_keypad):
    seq = ''
    v = 5
    for row in rows.split('\n'):
        v = get_digit(row, v, keypad)
        seq += str(v)
    return seq