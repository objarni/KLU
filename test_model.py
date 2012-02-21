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
        
    def test_that_knowledge_goes_up_after_finished_unit_work(self):
        self.model.add_developer('kalle', [5])
        self.model.step(2) # finishing takes 2 steps since amount of work is 9, and knowledge is 5
        knowledge = self.model.get_knowledge('kalle')
        self.assertEqual([6], knowledge)
        
    def test_works_on_unit_after_one_step(self):
        self.model.add_developer('kalle', [4])
        self.model.step(1)
        doing = self.model.get_doing('kalle')
        assert 'working on unit 0' == doing
       
if __name__ == '__main__':
    unittest.main()
