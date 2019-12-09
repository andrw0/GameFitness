# How to run GameFitness
## Environment requirements 

- Python 3.7
- Pip 19.2.3

## running the application

- navigate to the program root folder 

```
.\src\gamefitnessweb>
```

- install virtualenv

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

- navigate into the application folder 

```
.\src\gamefitnessweb\gamefitnessweb>
```

- run pytest

```
pytest
```

Below is what should occur when you run the tests 

***PUT TESTS SCREEN HERE ONCE ITS WORKING***

## Coverage

- navigate to the application folder

```
.\src\gamefitnessweb\gamefitnessweb>
```

- test coverage 

```
pytest --cov=gamefitnessweb
```

The test coverage screen should look like this:

***PUT COVERAGE SCREEN HERE ONCE ITS WORKING***



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
- Atheletes, Sports Enthusiast
 
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
 
 
 ## [Burndown Chart](https://app.zenhub.com/workspaces/gamefitness-5d9e317e1d8f2a00016ad9b7/reports/burndown?milestoneId=4737340)
 
 A snapshot of the burndown can be seen below:
 
 ![Scrum Board](https://github.com/shankarchandru/GameFitness/blob/master/RepoFiles/ScrumBoard.jpg "Scrum Board")
 
 
 
 
 
 
 
