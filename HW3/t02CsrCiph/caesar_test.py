from HW3.t02CsrCiph.caesar_logic import encrypt, decrypt
from unittest import TestCase, main


class Tester(TestCase):
    def test_encrypt_1(self):
        self.assertEqual(encrypt(3, "Hello world"), "Khoor zruog")

    def test_encrypt_2(self):
        self.assertEqual(encrypt(20, "I am the best programmer in the world"), "C ug nby vymn jlialuggyl ch nby qilfx")

    def test_encrypt_3(self):
        self.assertEqual(encrypt(-1, "aacz"), "zzby")

    def test_decrypt_1(self):
        self.assertEqual(decrypt(3, "Khoor zruog"), "Hello world")

    def test_decrypt_2(self):
        self.assertEqual(decrypt(3, "L dp wkh ehvw surjudpphu lq wkh zruog"), "I am the best programmer in the world")


main()
