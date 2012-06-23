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

    def test_becomes_expert_in_all_areas(self):
        team = klu.team(1)
        project = klu.project(2)
        project.add_tasks([0,1]*1000)
        klu.run(project=project,team=team,level=1)
        programmer = team.member[0]
        programmer_knowledge = programmer.level
        self.assertEqual([9,9], programmer_knowledge)

    def test_single_area_two_programmers_symmetry(self):
        team = klu.team(2)
        project = klu.project(1)
        project.add_random_tasks(1000)
        klu.run(project=project,team=team,level=5)
        programmer = team.member[0]
        programmer_knowledge = programmer.level
        self.assertEqual([5], programmer_knowledge)

    def test_single_area_first_programmer_becomes_expert(self):
        team = klu.team(2)
        project = klu.project(2)
        project.add_tasks([0,1] + [0]*10)
        klu.run(project=project,team=team,level=5)
        programmer = team.member[1]
        programmer_knowledge = programmer.level
        self.assertEqual([8,4], programmer_knowledge)

    def test_two_programmers_two_areas_random_tasks_empiric(self):
        team = klu.team(2)
        project = klu.project(2)
        project.add_random_tasks(1000,seed=19)
        klu.run(project=project,team=team,level=5)
        programmer = team.member[1]
        programmer_knowledge = programmer.level
        self.assertEqual([8,9], programmer_knowledge)

if __name__ == '__main__':
    unittest.main()
