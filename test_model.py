import unittest

from model import Model

class TestSingleDeveloperSingleUnit(unittest.TestCase):
    def test_that_developer_becomes_master_after_enough_time(self):
        model = Model(units = 1, ask_threshold = 3, todo = [0]*10000)
        model.add_developer('kalle', [1])
        model.step(1000)
        knowledge = model.get_knowledge('kalle')
        self.assertEqual([9], knowledge)
        
    def test_knowledge_unchanged_after_no_time_passed(self):
        model = Model(units = 1, ask_threshold = 3, todo = [0]*10000)
        model.add_developer('kalle', [5])
        knowledge = model.get_knowledge('kalle')
        self.assertEqual([5], knowledge)
