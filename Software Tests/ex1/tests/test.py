import unittest
import os
from src.file import create_file, write_to_file, read_from_file


class TestFileOps(unittest.TestCase):

    def test_create_file(self):
        filename = "test_create.txt"
        create_file(filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_write_to_file(self):
        filename = "test_write.txt"
        write_to_file(filename, "Hallo")
        with open(filename, "r") as f:
            self.assertEqual(f.read(), "Hallo")
        os.remove(filename)

    def test_read_from_file(self):
        filename = "test_read.txt"
        with open(filename, "w") as f:
            f.write("ABC")
        content = read_from_file(filename)
        self.assertEqual(content, "ABC")
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
