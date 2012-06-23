import unittest
import klu

class TestForSingleProgrammer(unittest.TestCase):
    def test_becomes_expert_after_enough_time(self):
        team = klu.team(1)
        project = klu.project(1)
        project.add_random_tasks(1000)
        klu.run_simulation(project = project, team = team)
        programmer = team.member[0]
        programmer_knowledge = programmer.level
        self.assertEqual([9], programmer_knowledge)

if __name__ == '__main__':
    unittest.main()
