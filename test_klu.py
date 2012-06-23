import unittest
import klu

class TestForSingleProgrammer(unittest.TestCase):
    def test_becomes_expert_after_enough_time(self):
        team = klu.team(1)
        project = klu.project(1)
        project.add_random_tasks(1000)
        klu.run(project=project,team=team)
        programmer = team.member[0]
        programmer_knowledge = programmer.level
        self.assertEqual([9], programmer_knowledge)
    def test_no_expertise_in_nonpracticed_area(self):
        team = klu.team(1)
        project = klu.project(2)
        project.add_tasks([0]*1000)
        klu.run(project=project,team=team,level=1)
        programmer = team.member[0]
        programmer_knowledge = programmer.level
        self.assertEqual([9,1], programmer_knowledge)

if __name__ == '__main__':
    unittest.main()
