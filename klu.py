#!/usr/local/bin/python
# coding: utf-8

# (K)nowledge (L)evel (U)p module

from operator import itemgetter
from collections import deque
import random

maxlevel       = 9
minlevel       = 1
default_level  = 5
default_effort = 9

def run(project,team,level=default_level):
    team.familiarize(project,level)
    time = 0

    while project.todo:
        while team.available and project.todo:
            team.assign(project)

        while project.ongoing:
            if team.available and project.todo:
               break
            team.workcycle(project)
            
            print "Time =", time
            project.progress()
            team.rollcall()
            project.upcoming()
            time += 1

    #print
    #print "Finished after", time, "work cycles."
    #print
    
    return time

class task:
    def __init__(self,area):
        self.area   = area
        self.effort = default_effort
        self.responsible = []
        self.consulted   = []

class project:
    def __init__(self,number_of_areas,effort=default_effort):
        self.area = []
        for i in range(number_of_areas):
            self.area.append(default_effort)
        self.todo = deque([])
        self.ongoing = []
    def add_tasks(self,list_of_tasks):
        for t in list_of_tasks:
            self.todo.append(task(t))
    def add_random_tasks(self,number_of_tasks,seed=[]):
        if seed:
            random.seed(seed)
        for i in range(number_of_tasks):
            t = int(len(self.area)*random.random())
            self.todo.append(task(t))
    def upcoming(self,number_of_tasks=10):
        l = []
        for i in range(min(number_of_tasks,len(self.todo))):
            l.append(str(self.todo[i].area))
        print 'Next %i task areas: %s' % (number_of_tasks, ' '.join(l))
    def progress(self):
        print 'Ongoing tasks:'
        for t in self.ongoing:
            print 'Area %i has %i effort left. Responsible programmer: %s.' % (t.area, t.effort, t.responsible.name)
    def finalize(self):
        self.ongoing[:] = [task for task in self.ongoing if task.effort > 0]

class programmer:
    def __init__(self,name,number_of_areas=0):
        self.name = name
        self.level = []
        self.status = 'free'
        for i in range(number_of_areas):
            self.level.append(default_level)
    def __getitem__(self,key):
        return self.level[key]
    def learn(self,level=default_level):
        self.level.append(level)
    def working(self):
        self.status = "working"
    def discussing(self):
        self.status = "discussing"
    def free(self):
        self.status = "free"
    def levelup(self,area):
        if self.level[area] < maxlevel:
            self.level[area] += 1
    def leveldown(self,area):
        if self.level[area] > minlevel:
            self.level[area] -= 1

class team:
    def __init__(self,number_of_programmers):
        self.member = []
        for i in range(number_of_programmers):
            p = programmer(str(i))
            self.member.append(p)
        self.available = []
        for i,p in enumerate(self.member):
            self.available.append(p)
    def familiarize(self,project,level=default_level):
        for i, p in enumerate(self.member):
            for i in range(len(project.area)):
                p.learn(level)
    def rollcall(self):
        for i, p in enumerate(self.member):
            print 'Programmer %s knowledge: %s [%s]' % (p.name, p.level, p.status)
    def get_knowledge_matrix(self):
        matrix = []
        for p in self.member:
            matrix.append(list(p.level))
        return matrix
    def assign(self,project):
        a = self.available
        t = project.todo
        if a and t:
            self.available = sorted(a, key=itemgetter(t[0].area))
            t[0].responsible = self.available.pop()
            t[0].responsible.working()
            project.ongoing.append(project.todo.popleft())
        else:
            print "No tasks or programmers available!"
    def workcycle(self,project):
        for i, task in enumerate(project.ongoing):
            task.effort -= task.responsible.level[task.area]
            if task.effort <= 0:
                for i, p in enumerate(self.member):
                    if p is task.responsible:
                        p.levelup(task.area)
                    else:
                        p.leveldown(task.area)
                self.available.append(task.responsible)
                task.responsible.free()
        project.finalize()







