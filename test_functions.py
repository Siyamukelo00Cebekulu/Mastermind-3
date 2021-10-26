import unittest
from unittest.mock import patch
from io import StringIO
import sys

from fileinput import filename
# from mastermind2 import get_input
from test_base import captured_io
import mastermind

class test_mastermind(unittest. TestCase):
    filename = "stuff.txt"
    sys.stdout = open(filename, "w")
    
    def test_create_code(self):
        count = 0
        while count == 100:
            code = mastermind.create_code()
            self.assertEqual(len(code), 4)  # 
            self.assertEqual(True, all( (numbers in range(1,9)) for numbers in code))
            self.assertEqual(True, all((code.count(number) == 1) for number in code))
            count += 1
    def test_check_correctness(self):     
            orig_stdout = sys.stdout
            new_string = StringIO()
            sys.stdout = new_string 
            for correct_digits_and_position in range(5):
                correctness = mastermind.check_correctness(0, correct_digits_and_position)
                if correct_digits_and_position == 4:
                    self.assertTrue(correctness)
                else:
                    self.assertFalse(correctness)
            sys.stdout = orig_stdout


    # with captured_io(StringIO("123\n12345\n1234\n"))
    # @patch("sys.stdin",StringIO("123\n12345\n1234\n"))
    def test_get_answer_input(self):   
        with captured_io(StringIO("123\n12345\n1234\n"))  as (out , err):

            mastermind.get_input()


        output = out.getvalue().strip() 
        # orig_stdout = sys.stdout

        # new_string = StringIO()
        # sys.stdout = new_string
        # answer = mastermind.get_input()
        # out = new_string.getvalue()
        
        self.assertEqual("Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:",output)
        # sys.stdout = orig_stdout


    @patch("sys.stdin",StringIO("3517\n6573\n6473\n6483\n6482\n"))
    def test_take_turn(self):
        
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,0))




                
                          

if __name__ == '__main__':
    unittest.main()

