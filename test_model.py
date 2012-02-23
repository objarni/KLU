# coding: utf-8
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
        
    def ignore_test_works_on_the_unit_after_one_step(self):
        self.model.add_developer('kalle', [4])
        self.model.step(1)
        doing = self.model.get_doing('kalle')
        assert 'working on unit 0' == doing
       
# med en utvecklare och två enheter:
# - blir utvecklaren expert
#   på båda givet tillräckligt lång tid (och uppgifter på båda!)
#   (2 tester)
#V- jobbar han enligt todo-listans ordning
#V  (1 test)
#V- det tar 9 steg att bli klar med en uppgift
#V  om kunskapsläget är 1 från början
#V  (1 test)
#V- det tar 1 steg att bli klar med en uppgift
#V  om kunskapsläget är 9 från början
class TestSingleDeveloperTwoUnits(unittest.TestCase):
    def setUp(self):
        self.model = Model(units = 2, ask_threshold = 3, todo = [0, 1]*1000)

    def test_finishes_task_in_one_step_if_master(self):
        self.model.add_developer('kalle', [9, 9])
        self.model.step(1)
        self.assertEqual('working on unit 1', self.model.get_doing('kalle'))

    def test_finishes_task_in_one_step_if_master(self):
        self.model.add_developer('kalle', [9, 9])
        self.model.step(1)
        self.assertEqual('working on unit 1', self.model.get_doing('kalle'))

    def test_finishes_task_in_9_steps_if_newbee(self):
        self.model.add_developer('kalle', [1, 1])
        self.model.step(9)
        self.assertEqual('working on unit 1', self.model.get_doing('kalle'))

    def test_works_in_todo_order(self):
        self.model.add_developer('kalle', [9, 9])
        work_order = []
        work_order.append(self.model.get_doing('kalle')[-1])
        self.model.step(1)
        work_order.append(self.model.get_doing('kalle')[-1])
        self.model.step(1)
        self.assertEqual(['0', '1'], work_order)

if __name__ == '__main__':
    unittest.main()




