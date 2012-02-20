import unittest

from model import Model

class TestSingleDeveloperTests(unittest.TestCase):
    def test_becomes_master_after_enough_time_passed(self):
        model = Model(units = 1, ask_threshold = 3)
        model.add_developer([1])
        model.step(1000)
        knowledge = model.get_knowledge(0)
        assert knowledge = 9
