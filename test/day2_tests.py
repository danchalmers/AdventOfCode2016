import unittest

from day2 import get_digit, get_digits, pt2_keypad


class KeypadTest(unittest.TestCase):

    def test_get_digit_ul(self):
        LINE = 'UL'
        digit = get_digit(LINE)
        self.assertEqual(1, digit)

    def test_get_digit_dr(self):
        LINE = 'DR'
        digit = get_digit(LINE)
        self.assertEqual(9, digit)

    def test_get_digit_edge_limit_high(self):
        LINE = 'RRRDDD'
        digit = get_digit(LINE)
        self.assertEqual(9, digit)

    def test_get_digit_edge_limit_low(self):
        LINE = 'ULULUL'
        digit = get_digit(LINE)
        self.assertEqual(1, digit)

    def test_get_digit_offset_start(self):
        LINE = 'DLLUR'
        digit = get_digit(LINE, 6)
        self.assertEqual(5, digit)

    def test_get_digit_seq(self):
        INSTRUCTIONS = '''ULL
RRDDD
LURDL
UUUUD'''
        seq = get_digits(INSTRUCTIONS)
        self.assertEqual('1985', seq)

    def test_limit_keypad(self):
        INSTRUCTIONS = '''ULL
RRDDD
LURDL
UUUUD'''
        seq = get_digits(INSTRUCTIONS, keypad=pt2_keypad)
        self.assertEqual('5DB3', seq)


INPUT = '''LLRRLLRLDDUURLLRDUUUDULUDLUULDRDDDULLLRDDLLLRRDDRRUDDURDURLRDDULRRRLLULLULLRUULDLDDDUUURRRRURURDUDLLRRLDLLRRDRDLLLDDRRLUDDLDDLRDRDRDDRUDDRUUURLDUDRRLULLLDRDRRDLLRRLDLDRRRRLURLLURLRDLLRUDDRLRDRRURLDULURDLUUDURLDRURDRDLULLLLDUDRLLURRLRURUURDRRRULLRULLDRRDDDULDURDRDDRDUDUDRURRRRUUURRDUUDUDDDLRRUUDDUUDDDUDLDRDLRDUULLRUUDRRRDURLDDDLDLUULUDLLRDUDDDDLDURRRDRLLRUUUUDRLULLUUDRLLRDLURLURUDURULUDULUDURUDDULDLDLRRUUDRDDDRLLRRRRLDRRRD
DRRRDULLRURUDRLRDLRULRRLRLDLUDLUURUUURURULRLRUDRURRRLLUDRLLDUDULLUUDLLUUUDDRLRUDDDDLDDUUDULDRRRDULUULDULDRUUULRUDDDUDRRLRLUDDURLLDRLUDUDURUUDRLUURRLUUUDUURUDURLUUUDRDRRRDRDRULLUURURDLUULLDUULUUDULLLDURLUDRURULDLDLRDRLRLUURDDRLDDLRRURUDLUDDDLDRLULLDRLLLURULLUURLUDDURRDDLDDDDRDUUULURDLUUULRRLRDLDRDDDRLLRUDULRRRUDRRLDRRUULUDDLLDUDDRLRRDLDDULLLRDURRURLLULURRLUULULRDLULLUUULRRRLRUDLRUUDDRLLLLLLLURLDRRUURLDULDLDDRLLLRDLLLDLRUUDRURDRDLUULDDRLLRRURRDULLULURRDULRUDUDRLUUDDDDUULDDDUUDURLRUDDULDDDDRUULUUDLUDDRDRD
RRRULLRULDRDLDUDRRDULLRLUUDLULLRUULULURDDDLLLULRURLLURUDLRDLURRRLRLDLLRRURUDLDLRULDDULLLUUDLDULLDRDLRUULDRLURRRRUDDLUDLDDRUDDUULLRLUUDLUDUDRLRUULURUDULDLUUDDRLLUUURRURUDDRURDLDRRDRULRRRRUUUDRDLUUDDDUDRLRLDRRRRUDDRLLRDRLUDRURDULUUURUULLRDUUULRULRULLRULRLUDUDDULURDDLLURRRULDRULDUUDDULDULDRLRUULDRDLDUDRDUDLURLLURRDLLDULLDRULDLLRDULLRURRDULUDLULRRUDDULRLDLDLLLDUDLURURRLUDRRURLDDURULDURRDUDUURURULLLUDDLDURURRURDDDRRDRURRUURRLDDLRRLDDULRLLLDDUDRULUULLULUULDRLURRRLRRRLDRRLULRLRLURDUULDDUDLLLUURRRLDLUDRLLLRRUU
URLDDDLDRDDDURRRLURRRRLULURLDDUDRDUDDLURURLLRDURDDRLRUURLDLLRDLRUUURLRLDLDRUDDDULLDULLDUULURLDRDUDRRLRRLULRDDULUDULDULLULDLRRLRRLLULRULDLLDULRRLDURRRRDLURDLUDUUUDLURRRRRUDDUDUUDULDLURRDRLRLUDUDUUDULDDURUDDRDRUDLRRUDRULDULRDRLDRUDRLLRUUDDRLURURDRRLRURULLDUUDRDLULRUULUDURRULLRLUUUUUDULRLUUDRDUUULLULUDUDDLLRRLDURRDDDLUDLUUDULUUULDLLLLUUDURRUDUDLULDRRRULLLURDURDDLRRULURUDURULRDRULLRURURRUDUULRULUUDDUDDUURLRLURRRRDLULRRLDRRDURUDURULULLRUURLLDRDRURLLLUUURUUDDDLDURRLLUUUUURLLDUDLRURUUUDLRLRRLRLDURURRURLULDLRDLUDDULLDUDLULLUUUDLRLDUURRR
RLLDRDURRUDULLURLRLLURUDDLULUULRRRDRLULDDRLUDRDURLUULDUDDDDDUDDDDLDUDRDRRLRLRLURDURRURDLURDURRUUULULLUURDLURDUURRDLDLDDUURDDURLDDDRUURLDURRURULURLRRLUDDUDDDLLULUDUUUDRULLLLULLRDDRDLRDRRDRRDLDLDDUURRRDDULRUUURUDRDDLRLRLRRDLDRDLLDRRDLLUULUDLLUDUUDRDLURRRRULDRDRUDULRLLLLRRULDLDUUUURLDULDDLLDDRLLURLUDULURRRUULURDRUDLRLLLRDDLULLDRURDDLLDUDRUDRLRRLULLDRRDULDLRDDRDUURDRRRLRDLDUDDDLLUDURRUUULLDRLUDLDRRRRDDDLLRRDUURURLRURRDUDUURRDRRUDRLURLUDDDLUDUDRDRURRDDDDRDLRUDRDRLLDULRURULULDRLRLRRLDURRRUL'''
print('pt 1 solution: %s' % get_digits(INPUT))
print('pt 2 solution: %s' % get_digits(INPUT, keypad=pt2_keypad))