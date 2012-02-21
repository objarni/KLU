import unittest

from model import Model

class TestSingleDeveloperSingleUnit(unittest.TestCase):
    def setUp(self):
        self.model = Model(units = 1, ask_threshold = 3, todo = [0]*10000)
        
    def test_that_developer_becomes_master_after_enough_time(self):
        self.model.add_developer('kalle', [1])
        self.model.step(1000)
        knowledge = self.model.get_knowledge('kalle')
        self.assertEqual([9], knowledge)
        
    def test_that_knowledge_unchanged_after_no_time_passed(self):
        self.model.add_developer('kalle', [5])
        knowledge = self.model.get_knowledge('kalle')
        self.assertEqual([5], knowledge)
