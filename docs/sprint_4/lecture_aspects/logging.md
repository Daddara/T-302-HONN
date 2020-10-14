# Log
**Task**
> Describe and include details how are you handling the logs so far. If you were to implement monitoring what are the top 5 components you would monitor and what metrics would you consider, justify your metrics by giving a brief description.   

## Definition
Logging describes the act of  


We also have some manual logging of important team decisions in the decision protocol for each sprint. 

## Current implementation and usage.
This section describes how we currently handle this topic in our software and team. We didn't setup a formal logging policy in out team. The current extend of logging is managed by the used framework, software, coder and the reviewer as a second pair of eyes.  

### Backend
Our current backend application used the standard output stream via the python `print` function. The backend code it self doesn't contain any print statements that were added by us. The current console output is a result of Djangos default implementation and contains:
* A startup message with the system status
* IP and Port information
* Requests with the time, date, url and result http status

Here is an example of such a log:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 14, 2020 - 14:04:28
Django version 3.1.1, using settings 'workout_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[14/Oct/2020 14:04:34] "GET / HTTP/1.1" 200 5094
Not Found: /favicon.ico
[14/Oct/2020 14:04:38] "GET /favicon.ico HTTP/1.1" 404 5425
[14/Oct/2020 14:04:45] "GET /static/main.css HTTP/1.1" 200 2661
[14/Oct/2020 14:04:56] "GET /static/main/images/cover.png HTTP/1.1" 200 61337
[14/Oct/2020 14:05:26] "GET /accounts/register/ HTTP/1.1" 200 6835
[14/Oct/2020 14:05:55] "POST /accounts/register/ HTTP/1.1" 302 0
[14/Oct/2020 14:05:55] "GET /accounts/login/ HTTP/1.1" 200 5718
[14/Oct/2020 14:06:02] "POST /accounts/login/ HTTP/1.1" 302 0
[14/Oct/2020 14:06:02] "GET / HTTP/1.1" 302 0
[14/Oct/2020 14:06:02] "GET /dashboard/ HTTP/1.1" 200 9920
[14/Oct/2020 14:06:02] "GET /static/exercise/css/exercise.css HTTP/1.1" 200 768
[14/Oct/2020 14:06:02] "GET /static/weather/css/weather.css HTTP/1.1" 200 413
[14/Oct/2020 14:06:03] "GET /static/workout/js/rate_exercise.js HTTP/1.1" 200 3294
```

Exceptions in our application are handled in a similar way. Django catches these prints the stack trace and returns 500 (Internal Server Error) to the requester. Here is a shortened example log of an error:
```
[14/Oct/2020 14:06:03] "GET /static/workout/js/rate_exercise.js HTTP/1.1" 200 3294
Internal Server Error: /api/weather/v1/current
Traceback (most recent call last):
  [...]
  File "C:\Users\frist\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  [...]
  File "C:\Users\frist\AppData\Local\Programs\Python\Python38-32\lib\urllib\request.py", line 1353, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
[14/Oct/2020 14:06:03] "GET /api/weather/v1/current HTTP/1.1" 500 144992
```

We also use the default implementation of the Django migration log. Here is a shortened of such a log: 
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, payment, sessions, user, wallet, workout
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
```

### Frontend
Out frontend is self contains very little logic in comparison to the backend. We try to keep all the rendering logic in the backend and use Django's template system for the layout. The three exceptions for this rule is the rating system, weather display and payment system. These systems write a small amount of information into the web console of the browser. This is used for development to make sure that the frontend event was interpreted correctly. Here is an example for rating 3 workouts this example contains no log message from the weather display which means that no errors occurred in that script.
```
Workout update 1 +1                         workouts:448:17
Workout update 1 -1                         workouts:448:17
Workout update 5 +1                         workouts:448:17
```   

This log contains the message origin by default. This is a functionality in Firefox and Chromium.

### Testing
The test in our application write a minimal amount of messages to the console. A message usually states what is being tested, the result code of the request and an `OK` if the result was expected. A full test run using [`run-coverage.sh`](run-coverage.sh) adds a coverage report to the end of the run. This console output is kept as a part of the GitLab pipeline. Here is a shortened example of such a log:

```sh
$ sh run-coverage.sh
Note: Don't forget to migrate your database (workoutapp/reset_db.sh)
Creating test database for alias 'default'...
.................................
----------------------------------------------------------------------
Ran 33 tests in 9.007s
OK
Destroying test database for alias 'default'...
System check identified no issues (0 silenced).
[...]
Testing user registration: 201, OK
Testing that wallet returns a view: 200, OK
Testing Fitcoin information like the exchange rateTesting wallet balance: 200, OK
Testing if wallet exists: True, OK
.....
----------------------------------------------------------------------
Ran 5 tests in 1.364s
OK
Name                                                    Stmts   Miss  Cover
---------------------------------------------------------------------------
[...]
workout/migrations/__init__.py                              0      0   100%
workout/models.py                                          99     22    78%
workout/tests.py                                           64      7    89%
workout/urls.py                                             3      0   100%
---------------------------------------------------------------------------
TOTAL                                                    1554    224    86%
exit with status:  0
```
[Source](https://gitlab.com/xFrednet/t-302-honn-2020-team-9/-/jobs/777881562)

### Team activity
We're required to provide a decision and and retrospective protocol for our them. The decision protocol is also called decision log. The goal of this artefact is to list all complex and major decisions that were made by the team during the development phase. This is not the focus of this task but maybe still worth documenting.

The decision log has to be created manually. We usually assign one member of the group at the start of the sprint to write the decision protocol for the sprint duration. This team member is than responsible to create the log and merge requests to add them into master. The MR reviewer is also responsible to check that all important decisions are written down.

The retrospective protocol is assigned at the meeting it self. This protocol is reviewed in the same fashion like the decision protocol.

## Top 5 components to monitor and their metrics

1. Frontend
2. Payment (critical)
3. Data creation
4. Access logging
5. Like and Dislike system
6. IDK and IDC