import unittest

from func import sum

class TestSum(unittest.TestCase):
	def test_list_int(self):
		#data = [1,2,3]
		result = sum(1,2)
		self.assertEqual(result, 3)

if __name__ == '__main__':
	unittest.main()
