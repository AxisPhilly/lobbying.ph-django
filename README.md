#Lobbying.ph-django
This is the active repo for http://lobbying.ph, a tool to help journalists and citizens better understand and access Philadelphia [lobbying reports](http://www.phila.gov/ethicsboard/lobbying.html).

This project is supported by the Philadelphia Public Interest Information Network.

The original Sinatra/Ruby version of the site (https://github.com/caseypt/lobbying.ph) was used as a prototype and is no longer maintained.

##Dependencies

- Python
- [VirtualEnv](http://www.virtualenv.org/en/latest/index.html)
- [PostgreSQL](http://www.postgresql.org/)
- [Memcached](http://www.memcached.org)
- [ElasticSearch](http://www.elasticsearch.org/)
- [Compass](http://compass-style.org/)
- [Sass](http://sass-lang.com/)

##Getting Started

1. Install the external dependencies listed above.
2. Make sure the required services are running (PostreSQL, Memcached, ElasticSearch, Compass).
3. Create a virtual environment: `virtualenv venv`
4. Activate the virtual enviornment: `source venv/bin/activate`
5. Install the project dependencies: `pip install -f requirements.txt`
6. Start the Django server: `python manage.py runserver`
7. Go to `http://localhost:8000` to view the site