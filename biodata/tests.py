from django.test import TestCase

class ContohTest(TestCase):
    def test_matematika_dasar(self):
        # Tes super simpel agar pytest tidak kosong
        self.assertEqual(1 + 1, 2)