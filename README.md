# Cornershop's Backend Test

This technical test requires the design and implementation (using Django) of a basic management system to coordinate the meal delivery for Cornershop employees.

- [Test's Definitions](<https://github.com/gegonzalez/Backend-Test-Gonzalez/blob/master/docs/Context.md>)

## Tech Stack

- [Django 3.0.6](<https://www.djangoproject.com/>)
- [Python 3.8.3](<https://www.python.org/downloads/>)

## Applications

There are two applications in this project:

- **Menu**: defines the features related to the Menus
- **Accounts**: handles administration for Users

## How to install and run

1. Set the enviroment variable `SLACK_WEBHOOK_URL_CRONTAB` with the webhook of the Slack channel
2. Execute the command `make run`
3. Open the link <http://127.0.0.1:8000/>
4. Super User can be created with `make createsuperuser`

## App Commands

- `python3 manage.py migrate`: Execute migrations
- `python3 manage.py makemigrations appName`: Create migrations for an App
- `python3 manage.py runserver 8080`: Run local server
- `python3 manage.py test appName -v 2`: Run test for an App
- `pytest`: Show the test coverage report

## User Especifications

- The Application is configured for a logged user to be Nora, and assumes that the rest of the non logged users are Employees. So, they can use the reminder link to make their orders.

## Cronjob Especification

There is a job configured to send the reminder every day at 9 am CLT. In order to work, It is required to make the next configurations:

1. Set the enviroment variable `SLACK_WEBHOOK_URL_CRONTAB` with the webhook of the target channel
2. Add the cronjob by executing the next command `python3 manage.py crontab add`

After making the configurations, It can be tested by executing `python3 manage.py crontab run [jobhash]`

### Cronjob commands

- `python3 manage.py crontab add`: Adds a job to crontab (of the user which you are running this command with)
- `python3 manage.py crontab show`: show current active jobs of this project
- `python3 manage.py crontab remove`: Remove all active jobs
