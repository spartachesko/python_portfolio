import unittest
from Development_cycle_support.bowling import get_score


class BowlingTest(unittest.TestCase):
    # проверка на количество фреймов в игре
    def test_quality_frames_new(self):
        # фреймов больше 10
        with self.assertRaises(Exception):
            get_score(game_result='12345123115472819-X44', status='new')
        # фреймов меньше 10
        with self.assertRaises(Exception):
            get_score(game_result='12345123115472819-', status='new')





    def test_quality_frames(self):
        # фреймов больше 10
        with self.assertRaises(Exception):
            get_score(game_result='12345123115472819-X44', status='old')
        # фреймов меньше 10
        with self.assertRaises(Exception):
            get_score(game_result='12345123115472819-', status='old')

    def test_position_slash_new(self):
        # проверка о наличии spare на первой позиции в фрейме
        with self.assertRaises(Exception):
            get_score(game_result='12/45123115472819-X', status='new')

    def test_position_slash(self):
        # проверка о наличии spare на первой позиции в фрейме
        with self.assertRaises(Exception):
            get_score(game_result='12/45123115472819-X', status='old')

    def test_double_slash_new(self):
        # проверка о наличии двойного spare
        with self.assertRaises(Exception):
            get_score(game_result='12//5123115472819-X', status='new')

    def test_double_slash(self):
        # проверка о наличии двойного spare
        with self.assertRaises(Exception):
            get_score(game_result='12//5123115472819-X', status='old')

    def test_incorrect_symbols_new(self):
        # проверка о наличии двойного spare
        with self.assertRaises(Exception):
            get_score(game_result='1.5123115472819-X12', status='new')

    def test_incorrect_symbols(self):
        # проверка о наличии двойного spare
        with self.assertRaises(Exception):
            get_score(game_result='1.5123115472819-X12', status='old')

    def test_quality_skittles_in_frame_new(self):
        # проверка количества кегель во фрейме
        with self.assertRaises(Exception):
            get_score(game_result='12345523115472819-X', status='new')
        with self.assertRaises(Exception):
            get_score(game_result='12349923115472819-X', status='new')

    def test_quality_skittles_in_frame(self):
        # проверка количества кегель во фрейме
        with self.assertRaises(Exception):
            get_score(game_result='12345523115472819-X', status='old')
        with self.assertRaises(Exception):
            get_score(game_result='12349923115472819-X', status='old')

    # проверка корректности калькуляции для внешнего рынка
    def test_correct_input_score_new(self):
        result = get_score(game_result='3532X332/3/62--62X', status='new')
        self.assertEqual(result, 90)

        result = get_score(game_result='4-3/7/3/8/X711627-5', status='new')
        self.assertEqual(result, 119)

        result = get_score(game_result='3-6/5/9/5---1/--5-52', status='new')
        self.assertEqual(result, 79)


    # проверка корректности калькуляции для внутреннего рынка
    def test_correct_input_score(self):
        result = get_score(game_result='3532X332/3/62--62X', status='old')
        self.assertEqual(result, 105)

        result = get_score(game_result='4-3/7/3/8/X711627-5', status='old')
        self.assertEqual(result, 113)

        result = get_score(game_result='3-6/5/9/5---1/--5-52', status='old')
        self.assertEqual(result, 80)


if __name__ == '__main__':
    unittest.main()
