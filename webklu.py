#!/usr/local/bin/python
# coding: utf-8

print "Content-Type: text/html; charset=utf-8"
print 
print "<html>"
print "<head>"
print "<title>KLU - asocial team</title>"
print "<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />"
print "</head>"
print "<body>"
print "<pre>"

import cgi
import cgitb
cgitb.enable()
params = cgi.FieldStorage()

import klu
print "--- (K)nowledge (L)evel (U)p ---"
print "<a href='desc.py'>Asocial team simulation</a>"
# Script parameters
def param(label, id, default):
    value = int(params.getfirst(id, str(default)))
    print '%30s: <input type="text" name="%s" value="%i"/><br />' % (label, id, value)
    return value

print '<form action="webklu.py" method="get">'
programmers  = param('Number of programmers', 'programmers', 2)
todolength   = param('Number of tasks', 'todolength', 150)
areas        = param('Number of areas', 'areas', 4)
initiallevel = param('Initial knowledge level', 'initiallevel', 5)
seed         = param('Random seed', 'seed', 19)

print '    <input type="submit" value="Run" /><br />'

print '</form>'

number_of_areas = areas
number_of_tasks = todolength

project = klu.project(number_of_areas)
project.add_random_tasks(number_of_tasks,seed=seed)

team = klu.team(programmers)
time = klu.run(project = project, team = team, level = initiallevel)
'''
team.familiarize(project,level=initiallevel)
time = 0

while project.todo:
    while team.available and project.todo:
        team.assign(project)

    while project.ongoing:
        if team.available and project.todo:
            break
        team.workcycle(project)
        print
        print "Time =",time
        project.progress()
        team.rollcall()
        project.upcoming()
        time += 1

print
print "Finished after", time, "work cycles."
print

team.rollcall()
'''

def print_statistics(time, tasks, programmers):
    time_per_task = time / tasks
    time_per_programmertask = time*programmers/tasks
    print
    print "--- Statistics ---"
    print "Average time per task.."
    print "       ..team:  %1.2f (cycles/tasks)" % time_per_task
    print " ..programmer:  %1.2f (cycles*programmers/tasks)" % time_per_programmertask
    print

time = float(time)
tasks = float(todolength)
programmers = float(programmers)

print_statistics(time, tasks, programmers)

print "</pre>"
print "</body>"
print "</html>"

# TODO
# use klu.run
# add log-argument to klu.run
# script to upload to ftp


