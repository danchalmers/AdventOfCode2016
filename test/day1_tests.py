import unittest

from day1 import calc_step, Facing, calc_seq_dist, calc_seq_crossing


class ManhattanDistanceTest(unittest.TestCase):

    def test_one_step_e(self):
        INPUT = 'R1'
        x, y, f = calc_step(INPUT, 0, 0)
        self.assertEqual(1, x)
        self.assertEqual(0, y)
        self.assertEqual(Facing.e, f)

    def test_two_step_l(self):
        INPUT = 'L2'
        x, y, f = calc_step(INPUT, 0, 0)
        self.assertEqual(-2, x)
        self.assertEqual(0, y)
        self.assertEqual(Facing.w, f)

    def test_eleven_step_r(self):
        INPUT = 'R11'
        x, y, f = calc_step(INPUT, 0, 0)
        self.assertEqual(11, x)
        self.assertEqual(0, y)
        self.assertEqual(Facing.e, f)

    def test_one_step_not_from_origin_south(self):
        INPUT = 'L1'
        x, y, f = calc_step(INPUT, 1, 2, Facing.s)
        self.assertEqual(2, x)
        self.assertEqual(2, y)
        self.assertEqual(Facing.e, f)

    def test_one_step_not_from_origin_west(self):
        INPUT = 'R1'
        x, y, f = calc_step(INPUT, 2, 1, Facing.w)
        self.assertEqual(2, x)
        self.assertEqual(2, y)
        self.assertEqual(Facing.n, f)

    def test_sequence_one(self):
        INPUT = 'R2, L3'
        d = calc_seq_dist(INPUT)
        self.assertEqual(5, d)

    def test_sequence_two(self):
        INPUT = 'R2, R2, R2'
        d = calc_seq_dist(INPUT)
        self.assertEqual(2, d)

    def test_sequence_two(self):
        INPUT = 'R5, L5, R5, R3'
        d = calc_seq_dist(INPUT)
        self.assertEqual(12, d)

    def test_sequence_crosses_itself(self):
        INPUT = 'R8, R4, R4, R8'
        x, y = calc_seq_crossing(INPUT)
        self.assertEqual(4, x)
        self.assertEqual(0, y)
