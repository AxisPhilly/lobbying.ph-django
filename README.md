#Lobbying.ph-django
This is the active repo for [Lobbying.ph](http://lobbying.ph), a tool to help journalists and citizens better understand and access Philadelphia [lobbying reports](http://www.phila.gov/ethicsboard/lobbying.html).

The original Sinatra/Ruby version of the site (https://github.com/caseypt/lobbying.ph) was used as a prototype and is no longer maintained.

##Dependencies

- Python (see requirements.txt for project Python dependencies)
- [VirtualEnv](http://www.virtualenv.org/en/latest/index.html)
- [PostgreSQL](http://www.postgresql.org/)
- [Memcached](http://www.memcached.org)
- Libmemcached
- [ElasticSearch](http://www.elasticsearch.org/)
- [Compass](http://compass-style.org/)
- [Sass](http://sass-lang.com/)

##Getting Started

1. Install the external dependencies listed above. I'd recommend using [homebrew](http://mxcl.github.com/homebrew/)
2. Make sure the required services are running (PostgreSQL, Memcached, Libmemcached ElasticSearch, Compass). 
3. Create a virtual environment: `virtualenv venv`
4. Activate the virtual enviornment: `$ source venv/bin/activate`
5. Install the project dependencies: `$ pip install -f requirements.txt`
6. Set the following environment variables for use by Haystack:
  - `BONSAI_INDEX` to your ElasticSearch index name
  - `BONSAI_URL` to your ElasticSearch server URL, which defaults to `http://127.0.0.1:8000/`
7. Create the project database: `$ createdb lobbying`
8. Create the project database tables: `$ python manage.py syncdb --settings=project.settings_dev`
9. Create the `lobbyingph` app tables: `python manage.py migrate lobbyingph --settings=project.settings_dev`
10. Start the Django server: `$ python manage.py runserver --settings=project.settings_dev`
11. Go to `http://localhost:8000` to view the site
