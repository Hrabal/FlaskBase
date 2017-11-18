# FlaskBase
## Base structure for a flask project with a little magic.

This is a blueprint for every small-to-medium flask + SQLAlchemy projects. Designed to be cloned and used on the fly.

## Basic usage

git clone this repo, rename/reset the local clone and start building your project.

edit the config.py file to change the db settings (default is a SqlLite db named after the directory your project is in).

Site routes and URIs should be defined in the views directory, avery SQLAlchemy models file should be placed in the models subdirectory.

The static folder is divided into css, files img and js sobfolders, store your static resources here.

## Db commodities

Db migration scripts are based (well... stolen) from the great [Miguel Grinberg's The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database). Read this to understand what's happening.

For a quick start run the scripts:

Python3 db_create.py
Python3 db_migrate.py
Python3 db_upgrade.py

## Views magic

Every .py file in the views directory will be loaded and *executed*. That means that every @app.route registered in the views directory will be served.
