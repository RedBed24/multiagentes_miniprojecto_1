---
title: Readme
author: Samuel Espejo Gil
lang: en
date: 24/25
abstract: |
    Trabajo de Sistemas multiagentes para intregrar las tecnologías aprendidas en los primeros laboratorios.
    Se trata contenedores con docker, apis rest con fastapi, webscraping con beautifulsoup, orm con sqlalchemy y web con flask.
---
## Setup

### Python

Create a virtual enviroment for installing the dependencies.

``` bash
# create a virtual enviroment called .venv
python -m venv .venv

# activate the virtual environment
. .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

Run the fastapi app with:

```
fastapi dev src/main.py
```

To run some tests you can use pytest:

```
python -m pytest
```

### Database

You need docker installed, make sure it's running with:

```
systemctl start docker
```

Now you'll need the base mariadb docker image:

```
docker pull mariadb
```

And then, up the db with:

```
docker compose up
```

We're using docker compose because, we'll have to run some services like filling the database and providing the web server.

If you have a mariadb client installed, you can check the database connection with:

```
mariadb -h 127.0.0.1 -P 3306 -u root -pmulti
```
