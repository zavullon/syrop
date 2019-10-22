from unittest import TestCase


class TestIs_polynom(TestCase):
    def test_is_polynom(self):
        """
        unit test, that tests main.polynom function
        """
        from main import is_polynom
        self.assertTrue(is_polynom('racecar'))
