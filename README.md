# py-it-task-manager
Website (portfolio project), Mate academy. Created 2025/04/15. Deadline 2025/04/17 18:00.

** General information **

The purpose of the project is to arrange a project management of IT company. 
A worker is appointed to the position. Any worker can create tasks and assign 
them to himself of to other colleagues. The task status can be toggled 
(completed / not completed). The task can be of one or more types. The workers can
be organized to teams for solving projects. A project consists of one or more 
tasks. Project's status can be toggles similar to the task's status.
The task of any worker (or projects of a team) are shown, not finished first.

** Approach in general **

1. First worker is superuser.
2. Each worker is allowed to do all actions (no roles/restrictions so far). 
3. Each worker can create (invite) a new worker.
4. A worker can add a new position.
5. A worker has one position or has none.
6. Each task can has any number of type tasks.
7. Each task can be related to any number of workers, each worker can be related to any number of tasks.
8. Team is a group of workers (any number). One worker can be a member of several teams simultaneously.
9. Project is a batch of tasks (any number). Several teams can work on a project. 
10. One team can work on several projects at one time.
11. Team can be active or not. Status can be changed. Workers can join the team of leave it.
12. Task / project can be completed or not yet. Status can be changed.
13. At a worker page his (her) not completed and completed tasks are shown.

** Software requirements **

* Python 3.13 interpreter

Additional software:
* asgiref==3.8.1
* crispy-bootstrap4==2024.10
* Django==5.2
* django-crispy-forms==2.4
* sqlparse==0.5.3
* tzdata==2025.2

The following steps shall be made for installation of the additional software: 
* To open python terminal in the project directory,
* To run from the command line:
    pip install -r requirements.txt

Training database should be populated by running from the
command line:
    python manage.py loaddata.json

** Running the project **
To run from the terminal the command:
    python manage.py runserver
To enter the address in the search line of a browser 127.0.0.1.
To login as superuser with the credentials:
    Login: pc
    Password: 1qazcde3

Further steps are according to the site interface.




