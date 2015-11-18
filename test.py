import functions
import unittest

class MyTest(unittest.TestCase):
    def test_hello_user(self):
        result = functions.greeting()
        self.assertEqual('hello world',result)

    def test_hello_uppercase(self):
        name = "denver"
        result = functions.uppercase(name)
        self.assertEqual("Hello DENVER", result)

    def test_hello_joe(self):
        name = "Denver"
        result = functions.hello_joe(name)
        self.assertEqual('Hello Denver!',result)

    def test_number_list(self):
        result = functions.number_list(10)
        self.assertEqual([1,2,3,4,5,6,7,8,9,10], result)

    def test_sum_numbers(self):
        result = functions.sum_numbers(15)
        self.assertEqual(120, result)

    def test_length(self):
        string = "Denver"
        result = functions.stringLen(string)
        self.assertEqual(6, result)

    # def test_reverse(self):
    #     string = "Denver"
    #     result = functions.reverse(string)
    #     print result
    #     self.assertEqual("revneD", result)

    # def test_hello_list(self):
    #     number = 4
    #     result = functions.hello_list(number)
    #     self.assertEqual("Hello world Hello world Hello world Hello world", result)

    def test_low(self):
        numbers = [40,100, 1, 5, 25, 10]
        result = functions.low(numbers)
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
