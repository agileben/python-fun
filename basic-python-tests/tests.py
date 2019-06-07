import unittest

class MyThing:
    def add(self, num1, num2):
        return num1 + num2

class MyTest(unittest.TestCase):

  def test_pass(self):
      pass

  def test_add(self):
      thing = MyThing()
      self.assertEquals(thing.add(2, 2), 4)

