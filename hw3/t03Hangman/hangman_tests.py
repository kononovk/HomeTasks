from hw3.t03Hangman.hangman_logic import get_guessed_word, is_word_guessed
from unittest import TestCase, main


class Tester(TestCase):
    def test_1(self):
        self.assertEqual(get_guessed_word("apple", {'l', 'p'}), "_ p p l _ ")

    def test_2(self):
        self.assertEqual(get_guessed_word("programming", {'m', 'i', 'p'}), "p _ _ _ _ _ m m i _ _ ")

    def test_3(self):
        self.assertTrue(is_word_guessed("apple", {'a', 'p', 'l', 'e'}))

    def test_4(self):
        self.assertFalse(is_word_guessed("apple", {'a', 'p', 'l'}))


main()
