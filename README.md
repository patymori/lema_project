# LEMA - LL Employee Management

The purpose of this application is help Lab's team to manage employees' information.

## How it works

LEMA offers an admin WEB interface to manage employees' data and a REST API to list, add and remove employees.

## Getting Started

### Prerequisites
- GIT
- Python 3.6.1

`sudo apt-get install git python3.6.1 `

### Installation

1. Clone [LEMA project](https://github.com/patymori/lema_project.git) repository

`git clone https://github.com/patymori/lema_project.git`

2. Access project directory

`cd lema_project`

3. Create a Python Virtualenv and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Install project requirements
`pip install -r requirements.txt`

5. Create a Superuser to manage the system
`./manage.py createsuperuser`


## Running the project

`./manage.py runserver`


## Running Tests

`./manage.py test`


## How to use

Access Admin interface URL: `http://127.0.0.1:8000/admin`
