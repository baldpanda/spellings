import unittest

class SimpleTest(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(1,0)


### Need to make some sort of flask test infrastructure
###link to test skeleton
###http://flask.pocoo.org/docs/0.12/testing/

if __name__ =='__main__':
    unittest.main()
