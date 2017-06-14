# LEMA - LL Employee Management

The purpose of this application is help Lab's team to manage employees' information.

## How it works

LEMA offers an admin WEB interface to manage employees' data and a REST API to list, add and remove employees.

## Getting Started

### Prerequisites
- GIT must be installed
- Python 3.6.1

`sudo apt-get install git python3.6.1 `

### Installation

1. Clone [LEMA project](https://github.com/patymori/lema_project.git) repository

`git clone https://github.com/patymori/lema_project.git`

2. Access project directory

`cd lema_project`

4. Create a Python Virtualenv and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Run `setup.py` to install the project

`python setup.py`

## Running the project

`python3 manage.py runserver`


## Running Tests

`python3 manage.py test`


## Access to Admin interface
Create a superuser to access Admin interface

`python manage.py createsuperuser`
