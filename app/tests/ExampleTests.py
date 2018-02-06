import env
import json

from TestBase import TestBase

class ExampleTests(TestBase):

  def setUp(self):
    super(ExampleTests, self).setUp()

  # Tests
  def test_thing(self):
    self.assertTrue(True)


if __name__ == '__main__':
  import unittest
  unittest.main()
