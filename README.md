# Setup
## Install Mezzanine

    $ pip install mezzanine

## Setup adept

###  Create a database

        $ python manage.py createdb

### Fill in `SECRET_KEY` and `NEVERCACHE_KEY` in local_settings.py

###  Run the web server

        $ python manage.py runserver

### Create the homepage
1.  Log into the admin
2.  Go to Content -> Pages
3.  Click the top "Add ..." dropdown and choose "Home page"
4.  Fill out content, before saving click the "Meta data" section and set the url to /
5.  Save
