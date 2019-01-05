import unittest
from ExampleClassForUnitTest import Example


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE AFTER all methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
         print("This will run after every method")

    def test_add(self):
        result = Example.add(self, 10, 20)
        self.assertEqual(result, 30)

    def test_subtraction(self):
        result = Example.subtract(self, 10, 20)
        self.assertEqual(result, -10)


# if __name__ == '__main__':
#   unittest.main()
