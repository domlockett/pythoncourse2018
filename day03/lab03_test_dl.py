import unittest
from lab03_dl import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        self.assertEqual("PIG", shout("pig"))
      
    def test_reverse(self):
        self.assertEqual("gip", reverse("pig"))
       
    def test_reversewords(self):
        self.assertEqual('pig some', reversewords("some pig"))
     
    def test_reversewordletters(self):
        self.assertEqual("emos gip", reversewordletters("some pig"))
      
    def test_piglatin(self):
        self.assertEqual('ig-pay', piglatin("pig"))
      
if __name__ == '__main__':
  unittest.main()

