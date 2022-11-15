import unittest
import flask_whiteapp

class MyClassTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        # To be implemented if required
        pass

    def test_something(self):
        app = flask_whiteapp.create_app()
        self.assertTrue(True, True)