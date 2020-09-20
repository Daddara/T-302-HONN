# Workout with Team9
This is a website to manage sport activities. 
With this website it is possible to create a workout plan consisting out of several exercises.
You can publish these plans for others or challenge your friends to do them.
The goal is to inspire the user to work out by competition or just giving him the space to organize his workouts.
# Getting started
### Prerequisites
* Make sure you have installed the latest version of Python https://www.python.org/downloads/
* Install the latest version of PyCharm (IDE) https://www.jetbrains.com/pycharm/download/#section=windows
* Make sure you have installed the latest version of pip https://pip.pypa.io/en/stable/installing/
### Installing
* Clone the gitlab repository https://gitlab.com/xFrednet/t-302-honn-2020-team-9.git to an empty folder on your computer. 
Here is how: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
* Create a virtual environment in your project folder by following these steps:
    1. Open the "Workout app" folder in PyCharm
    2. Press Ctrl-Alt-S (Should open settings)
    3. Press the "Project" dropdown
    4. Press the "Python interpreter" menu
    5. In the top right hand side press the wheel and press add
    6. Select initialize new environment, select python as interpreter and press apply.
    7. Press ok when done.
    8. When you look at the terminal in PyCharm it should now say (venv) in front of C:\...
    9. If not, navigate into the folder venv/Scripts from terminal, type activate and press enter
* Install requirements (Should be prompted by IDE, if not install manually with `pip install -r requirements.txt`)
* Download the Django extension by running the command `pip install django`
# Populating the database
* While in the workoutapp directory type in terminal:
`py manage.py loaddata db.json`
* If your database is no longer empty you must first run:
`py manage.py flush`&
`yes`
# Running the server
* While in the workoutapp directory type in terminal: `py manage.py runserver`     
* If no errors pop up and the localhost link is displayed you are good to go
# Running the tests
* While in the workoutapp directory type in terminal: `py manage.py test`
# Built with
### Dependencies
`Python` `Pip` `Django`
The current list can be found in the [requirements.txt](requirements.txt)
### Framework
Django framework, see architecture [here](docs/project_overview/project_architecture.png)
### Lecture Aspects
* We are using the three-tier architecture taught in Lecture 03: Software Architecture
### Agreed Tasks

#### User stories
The following are user stories to implement agreed by the TA
* \#2 As a user I would like to be able to create and exercise that I can save and look at later.
* \#5 As a user, I would like to be able to create a new workout using the website
* \#9 As a user, I would like to be able to add exercises to my workout
* \#10 As a user, I want to be able to create an account
* \#11 As a user, I want to be able to log in and out of my account
* \#12 As a user I want to be able to add other users to a friends list
* \#13 As a user I want to be able to create a exercise plan for my exercises
* \#14 As a user I want to be able to edit my exercise plan and add/remove exercises to/from it.
* \#15 As a user I want to be able to decide whether my exercise plan is publicly visible or private
* \#16 As a user I want to be able to view my created exercises
* \#17 As a user I want to be able to view my create exercise plans
* \#18 As a user I want to be able to view public exercise plans
* \#19 As a user I want to be able to view public exercises
* \#20 As a user I want to be able to create challenges and tag my friends in them.
* \#23 As a user I want to be able to bookmark other users public plans/exercises 
* \#24 As a user I want to be able to give a rating to other peoples public plans/exercises
* \#25 As a user I would like to see which part of the body gets trained by an specific exercise
* \#27 As a user I want to follow other users to be able to subscribe to their public created exercises/plans
* \#29 As a user when I log in I want to see my dashboard
* \#35 As a user I would like to send direct messages to users on my friends list.
* \#36 As a user I would like to view my friends list.
* \#37 As a user I would like to see my notification inbox
* \#38 As a user I would like to be able to comment on a workout plan, so that I can voice my opinion on it.
* \#39 As a user, I want to be able to delete an exercise plan, so that I can remove plans I'm unhappy with
* \#40 As a user, I want to see a placeholder for deleted exercise plans that I bookmarked, so that I know that my favorite plan is no longer available
* \#43 As a user I would like to sort publicly available workouts by popularity (clicks) so that I can see what others like.
* \#45 As a user I would like to search for workouts by name
* \#46 As a user I would like to be able to filter for public workouts by category so that I can see only what I'm interested in.
* \#49 As a developer, I would like have a building pipeline in gitlab, so that I can make sure that my MR doesn't cause any new bugs and doesn't reduce the code coverage

#### Definition of Done
For this first sprint we have agreed to implement user stories #10, #11 and #29.
The full definition of done you can read [here](DEFINITION_OF_DONE.md).


# Contributors
| GitLab Username          | Student name                  |
| ------------------------ | ----------------------------- |
| @Daddara                 | Arnar Már Brynjarsson         |
| @Maciuska                | Maciej Sierzputowski          |
| @valgerdur-asgeirsdottir | Valgerður Ásgeirsdóttir       |
| @hauks96                 | Ægir Máni Hauksson            |
| @ingunn19                | Ingunn Káradóttir             |
| @Kristjamar              | Kristján Mar Svavarsson       |
| @katrinviktoria          | Katrín Viktoría Hjartardóttir |
| @xFrednet                | Fridtjof Peer Stoldt          |
| @madsaken                | Hafliði Stefánsson            |

