# Jal-Stats

### An API Back-End for Tracking Stats

* Website location: **`https://rocky-falls-8228.herokuapp.com/`**
* Local deployment location: `localhost:[PORT]/` where `[PORT]` is usually `5000` for heroku local and `8000` for Django

## About This Service

### API Endpoints (all prefixed with /api/)

Verb   | URL                                       | Action
------ | ---                                       | -------
GET    | /activities                               | Show a list of all activities I am tracking, and links to their individual pages
POST   | /activities                               | Create a new activity for me to track.
GET    | /activities/{id}                          | Show information about one activity I am tracking, and give me the data I have recorded for that activity.
PATCH  | /activities/{id}                          | Update one activity I am tracking, changing attributes such as its name. Does not allow for changing tracked data.
DELETE | /activities/{id}                          | Delete one activity I am tracking. This should remove tracked data for that activity as well.
POST   | /activities/{activity_id}/stats           | Add tracked data for a day. The data sent with this should include the day tracked.
PUT    | /activities/{activity_id}/stats/{stat_id} | Override the data for a day already recorded.
DELETE | /activities/{activity_id}/stats/{stat_id} | Remove tracked data for a day.


Located at `host/` and also `host/questions/`, where `host` is the location of the server (usually `localhost:8000` if using Django's `runserver`; `https://rocky-falls-8228.herokuapp.com/` if accessing on the web).


## System Requirements

* To run locally, you will need to have **Python&nbsp;3** installed on your machine. See [Python's site](https://www.python.org/) for details.

* Clone this repo onto your computer; the below assumes you have kept the default folder name as `django`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* This app is set up to run on PostgreSQL. It is set it up to have a local (development) database named `jal_stats` with a user of `jal_stats` and a password of `password`. The database name, user, and password can all be configured to your preferences in the `django/jal_stats/jal_stats/settings.py` file. If you do not have PostgreSQL on your machine, [follow these instructions](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).

* **Running the site with Django** requires more command line. Navigate to `django/jal_stats` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

* **Running the site with your own heroku local/web** requires that you have your machine set up with [heroku and heroku toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [create a heroku account](https://signup.heroku.com/).
 * Once you have these installed and have a heroku account, navigate to the `django` directory and run the following commands (making note of and copying the secret key when it is generated):
 ```
 $ heroku create
 $ heroku config:set DJANGO_SETTINGS_MODULE=jal_stats.heroku_settings
 $ heroku config:set PYTHONPATH=jal_stats
 $ heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(50)]))'`
 ```

 * Now, create a new file in the `django` directory called `.env` with the following contents where `[your_secret_key]` is replaced with the secret key generated in the previous step:
 ```
 DATABASE_URL=postgres:///jal_stats
 DJANGO_SETTINGS_MODULE=jal_stats.heroku_settings
 PYTHONPATH=jal_stats
 SECRET_KEY=[your_secret_key]
 ```

 * Next, navigate to the `django` directory and run the following commands to first collect the static files (e.g., css files), and then deploy heroku locally (usually located at `localhost:5000`). Again, this will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.
 ```
 $ python jal_stats/manage.py collectstatic
 $ heroku local web
 ```

 * Once this is working, you can deploy and then view online by running the following:
 ```
 $ git push heroku master
 $ heroku ps:scale web=1
 $ heroku run jal_stats/manage.py migrate
 $ heroku open
 ```

 * Optionally load the fake data fixtures:
 ```
 $ heroku run jal_stats/manage.py loaddata activities
 $ heroku run jal_stats/manage.py loaddata stats
 ```
