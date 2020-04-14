import unittest

from actions.util.file_util import *


class UtilsTest(unittest.TestCase):

    def test_list_file(self):
        files = list_files("resources/avatars/professional/female")
        self.assertEqual(2, len(files))

    def test_get_random_file(self):
        file = get_random_file("resources/avatars/professional/female")
        self.assertIsNotNone(file)

    def test_is_image(self):
        self.assertTrue(is_image("/path/file.jpg"))

    def test_is_not_image(self):
        self.assertFalse(is_image("/path/doc.txt"))


if __name__ == '__main__':
    unittest.main()
