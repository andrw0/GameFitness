# How to run GameFitness
## Environment requirements 

- Python 3.7
- Pip 19.2.3

## running the application

- install virtualenv in the folder you want to store your application in

```
###MacOS and Linux
pip install --user virtualenv
###Windows
pip install --user virtualenv
```

- create a virtual environment 

```
###MacOS and Linux
Python -m venv env
###Windows
Python -m venv env
```

- Activate Virtual Environment

```
###MacOS and Linux
source env/bin/activate
###Windows
.\env\Scripts\activate
```

You will know if you are in the virtual environment if you have (env) to the left of the directory like below:

```
(env) C:\Users\Andrew\Desktop\gamefitness_website\GameFitness\src\gamefitnessweb>
```

- navigate to the program root folder 

```
.\GameFitness\src\gamefitnessweb
```


- install the needed dependancies

```
pip install -r requirements.txt
```

- Run the Django server

```
python manage.py runserver
```

If the server is running correctly, it should look like this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 08, 2019 - 22:51:57
Django version 2.2.6, using settings 'gamefitnessweb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- Access the application from http://127.0.0.1:8000/homepage/

- To close the application, use Ctrl+break or Ctrl+C to stop the server

- Deactivate the virtual environment after you are done

```
deactivate
```

## Running Tests

- navigate into the root folder 

```
.\GameFitness\src\gamefitnessweb>
```

- run pytest

```
pytest
```

Below is what should occur when you run the tests 

```
=============================== test session starts ===============================
platform win32 -- Python 3.7.5, pytest-5.2.2, py-1.8.0, pluggy-0.13.0
Django settings: gamefitnessweb.settings (from ini file)
rootdir: C:\Users\Andrew\Desktop\gamefitness_website\GameFitness\src\gamefitnessweb, inifile: pytest.ini
plugins: cov-2.8.1, django-3.7.0
collected 10 items

gamefitnessweb\tests\test_models.py ..                                       [ 20%]
gamefitnessweb\tests\test_views.py ....                                      [ 60%]
gamefitnessweb\tests\test_urls.py ....                                       [100%]

=============================== 10 passed in 1.47s ================================
```

## Coverage

- navigate to the root folder

```
.\GameFitness\src\gamefitnessweb>
```

- test coverage 

```
pytest --cov=gamefitnessweb
```

The test coverage screen should look like this:

```

=============================== test session starts ===============================
platform win32 -- Python 3.7.5, pytest-5.2.2, py-1.8.0, pluggy-0.13.0
Django settings: gamefitnessweb.settings (from ini file)
rootdir: C:\Users\Andrew\Desktop\testGameFitness\GameFitness\src\gamefitnessweb, inifile: pytest.ini
plugins: cov-2.8.1, django-3.7.0
collected 10 items

gamefitnessweb\tests\test_models.py ..                                       [ 20%]
gamefitnessweb\tests\test_views.py ....                                      [ 60%]
gamefitnessweb\tests\test_urls.py ....                                       [100%]

----------- coverage: platform win32, python 3.7.5-final-0 -----------
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
gamefitnessweb\__init__.py                                     0      0   100%
gamefitnessweb\admin.py                                       12      0   100%
gamefitnessweb\apps.py                                         1      1     0%
gamefitnessweb\forms.py                                       27      0   100%
gamefitnessweb\migrations\0001_initial.py                      9      0   100%
gamefitnessweb\migrations\0002_games_game_description.py       4      0   100%
gamefitnessweb\migrations\__init__.py                          0      0   100%
gamefitnessweb\models.py                                      33      0   100%
gamefitnessweb\settings.py                                    23      0   100%
gamefitnessweb\tests\test_models.py                           11      0   100%
gamefitnessweb\tests\test_urls.py                             14      0   100%
gamefitnessweb\tests\test_views.py                            27      0   100%
gamefitnessweb\urls.py                                         7      0   100%
gamefitnessweb\views.py                                       49     17    65%
gamefitnessweb\wsgi.py                                         4      4     0%
------------------------------------------------------------------------------
TOTAL                                                        221     22    90%


=============================== 10 passed in 1.88s ================================
```

## What did we learn about software development?

- Things don't go as planned, with errors and setbacks arising at every step. Therefore, flexibility and a level demeanor are key to solving problems and moving ahead with the project.

- Iterative development is useful in helping maintain the continual progress of a software development project. Without set iterations and milestones, it is easy to fall behind.

- Each group member brings different strengths to the project, so initially it is advantageous for teams to have roles tailored to each group member. However, the team and its members need to be flexible and break from their roles when needed to ensure the project's completion.


## Burndown Chart for Milestone 2

- You can view our burndown chart here:

https://docs.google.com/spreadsheets/d/1SnnpIKlNKqX9QRNbNsDdGtALHIMJ08jSjkO3Ry_KOWk/edit?usp=sharing

## User Stories

- As a sports enthusiast, I would want to be able to create a profile in the Game Fitness application so I can manage my profile and history

- As the application owner, I want to make sure that there are minimal bugs in the program so that the user experience is the best it can be

- As a application designer, I need to be able to create a database design to store information related to exercises and user profiles

- As a user, I want to be able to choose a game and get a list of exercises so I remain injury free

# What is Game Fitness?
 Application that recommends exercises based on sports activities to keep you healthy and ready for the game.

# Concept
  The idea of the application is primarily to create a profile for a user and pick a sports activity or multiple and based on his personal height, weight and BMI, provide a list of suggested exercies by cateogeries (stretching, strenght training etc.). The user can then perform this exercies for a certain period and provide more inputs on changes to his weight, BMI and other parameters.
 
# Team

The project team comprises of 3 (smart) members. As this is a small team, all of us plan to support all the different work (PO, Scrum Master, DEV, TESTING, Stake holder meet ups etc. at some point in the project).

- Andrew Shults (Product Owner/Lead Developer/Tester)
- Abdulmajeed Mesefir (Lead QA/Developer/StakeHolder Meet up)
- Shankar Chandrasekaran (Scrum Master/Developer/Tester)

This is a progressive team and we collaborate distributively using Git issues as can be seen in our estimates interaction.

# Project StakeHolder(s)

- Professor Wallace Chipidza
- Athletes, Sports Enthusiast
 
# Project Requirements

- Build an application which provides customized/personalized list of exercises for a user based on his personal preferences and traits.
- The application should be able to track progress of the user traits and provide a visualize representation of the history of changes
- The application should also be able to categorize exercises (general cardio training vs swimming/running as options)
- Provide a guided tutorial/video/link to perform exercises 
 
# Technologies Used

We plan to use 
- Python : Building Business logic and MVC architecture based web framework
- Django web framework, HTML, CSS, Javascript : UI components/visualization
- SQlite : Database Engine/Data store


# Agile Planning Section

## Project Milestones and Iterations

#### Project will have 2 Milestones each comprising of 2 Iterations (duration of  2 weeks) and 1 Stabilization week inbetween them ####

### [Milestone 1 (Release)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/board?releases=5d9e616fcec9b500015b5b1a&repos=210957147) 

Milestone 1 will be addressing the following parts of the application

1. Collect exercises information
2. User Enrollment and Login Module
3. Admin login and exercies Module
4. Initial database connection and storage of user and exercise information

Issues identified

1. [Support User enrollment(3)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/12)
2. [Support admin user input(3)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/13)
3. [User login and modify profile(5)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/11)
4. [Decide which sports to include(1)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/5)
5. [Identify common injuries and exercies by sport(1)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/6)
6. [Python functions to support connection to sqlite database(1)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/9)

## Milestone 1 Artifacts
- ### [Milestone 1 Presentation](https://github.com/shankarchandru/GameFitness/blob/master/Artifacts/SoftwareDevelopment_GameFitness-Milestone1.pptx)
- ### Milestone Summary
     - User SignIn/Enrollment Page and submission
     - Collect exercises and common sport injuries for 10 common games/sports
     - Document exercises and categories based on difficulty levels
     - Create Django web framework to support building web pages based on MVC pattern of Models - Controller - Views
     - Building Models for Users, Games, Exercises
     - Building Controllers(views.py) to visualize using Views (forms.py) to submit content
     - Design database tables and columns (scripts/Django models) for storing Games, Users, Exercies info into SQlite DB
     - Build pytest for Models created/available for pytest


### [Milestone 2  (Release)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/board?releases=5d9e61a0cec9b500015b5b1d&repos=210957147)

Milestone 2 will be addressing the following parts of the application
1. User profile management for users 
2. User feedback and manage user exercises based on updated list and feedback/difficulty level

Issues identified

1. [User profile management and feedback](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/1)
2. [Update existing routine based on user feedback](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/issues/shankarchandru/gamefitness/14)


## Scrum Meetings/Discussion Page
 
 ## Scrum Stand Up Meetings
  The stand ups are weekly 2 times
  
  - Monday 12-12:30 PM (30 minutes)
  - Thursday 12-12:30 PM (30 minutes)
  
  ![A snapshot of Scrum Stand up Calendar](https://github.com/shankarchandru/GameFitness/blob/master/RepoFiles/ScrumMeeting-CalendarSnapshot.jpg "Stand Up Meetings Calendar")
 
 [Scrum Board(Zenhub board)](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/board?repos=210957147)
 
 ![A Snapshot of Scrum Board](https://github.com/shankarchandru/GameFitness/blob/master/RepoFiles/ScrumBoard.jpg "Scrum Zenhub board")
 
 ## Velocity - Milestone 1 (40%)
 Total Days for Milestone1 : 30 
 Total Days for Milestone1 ( by velocity) : 12 days
 Work for Milestone1 : 12 days
 
 
 ## [Burndown Chart For Milestone 1](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/reports/burndown?milestoneId=4737340)
 
 A snapshot of the burndown can be seen below:
 
 ![Scrum Board](https://github.com/shankarchandru/GameFitness/blob/master/RepoFiles/ScrumBoard.jpg "Scrum Board")
 
 
 
 
 
 
 
