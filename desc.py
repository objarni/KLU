#!/usr/local/bin/python

print "Content-type: text/html"
print 

print """
<html>
<body>
<pre>--- (K)nowledge (L)evel (U)p "Asocial team" ---
<a href='webklu.py'><--Back to simulation</a>
<img src="http://olofbjarnason.se/asocial_team.jpg" />
</pre>

"KLU asocial team" is an experiment in simulating team software development.

<p>The simulation works like this.

<ul>
<li>The simulated software consists of A independent <i>areas</i>.
<li>The simulated project consists of an ordered list of <i>tasks</i>,
ordered by business priority.
<li>Each task consist of 9 <i>subtasks</i> or <i>units of work</i>. The task
is associated with changes to one specific area of the code.
<li>The team consists of P <i>programmers</i>.
<li>Each programmer has a <i>knowledge level</i> for each area of the software.
<li>The knowledge level is an integer 1, 2, .. 9, where 1 means almost no knowledge,
and 9 means almost full knowledge of the area.
</ul>

Each turn, every un-assigned programmer is assigned the next available task.
If several programmers are unassigned, the one with the highest knowledge level
is assigned the next task.
<p>
If a task is finished, the knowledge level increases for the programmer that
has done the task. He/she levels up. The rationale of that should be clear.
<p>
But when software is changed by someone else than you, the "mental model" of
that area of the software is slightly offset from the current state of the
software (because of the changes). To take this into account in the simulation,
all other programmers' knowledge level is decreased one step when the task is
finished.
<p>
In real software team development, there are several techniques to keep the
mental model intact or up-to-date for each programmer: code reviews, pair
programming, openness to interruptions (asking questions/discussing things
often), and so on. However, in this simple simulation, we assume the team
is completely "robotic" and do not discuss the software with each other.
That's why we call it <i>the asocial team</i>.
<p>
The speed in which a task is completed depends solely on the knowledge level
of the programmer working on the task. For example, a programmer with knowledge
9 in the area of the task will solve it in one turn, since each task is 9 units of work.
A programmer with knowledge 2 will take 5 whole turns to finish
the same task. Tasks are always 9 units big, so the slowest a task can be
completed is in 9 turns.
<p>
This means that programmers working a lot on one area of the code will
get fast doing changes to that piece of code. A consequence of the knowledge
decrease among the other developers is that they will be slower working in
that area.
<p>
<u><b>Possible modifications to this simulation</b></u>
<ul>
  <li><b>Social team.</b> Adding a way for low-knowledge programmers to ask and learn from programmers
      with a higher knowledge would probably change the dynamics dramatically. If we
      add a threshold "question level", which means the level under which a programmer will
      ask questions about the area he/she is working on, we could view the asocial team
      as the social team with question level set to 1 (never ask questions). A programmer asking a question,
      will interrupt the other programmer, and none of them will get any effort done on their tasks that
      turn. However, the asking programmer would get a +1 in his/her level of knowledge instantly (by
      rationale it's easier to learn from a human explaning, than examining a software/source code system
      yourself, at least if the asked programmer knows much about the area in question). Also,
      the programmer answering questions will get a feeling of what is about to happen to the area,
      so he/she will not level down once that task is done for the low-level programmer.
  <li><b>Technical debt.</b> In asocial team simulation, no notion of good/bad-written code is included.
      There is a term for how badly written, or broke, a piece of code is: <i>technical debt</i>.
      If we say each area has a technical debt associated with it, and then categorize each programmer
      as a <i>sprinter</i>, <i>walker</i> or <i>crawler</i>, we could shift from a knowledge-based
      simulation to a debt simulation. A sprinter would work fast, but increase the debt of an area
      with 1. A walker would not work that fast, but wouldn't change the debt either, whereas a
      crawler would work slowly, but decrease the debt of the area once finishing a task. The effort
      for a task would depend on the technical debt of the tasks' area, so high technical debt
      would require more effort. An open question here would be if there is an upper level of how
      bad code can be written, that is if technical debt is limited to, say, 9, or not. Experience
      makes me ambivalent - code can be infinitely bad IMHO.
  <li><b>All of the above.</b> Combining <i>social team</i> with <i>technical debt</i> would probably
      be both hard to analyze and fun.
</ul>
</body>
</html>
"""
