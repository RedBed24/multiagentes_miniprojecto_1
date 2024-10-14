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

**This is an optional step as everything is dockerized.**

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

Run the web server using:

```
flask --app src.presentation.webui run
```

To run some tests you can use pytest:

```
python -m pytest
```

### Docker

You need docker installed, make sure it's running with:

```
systemctl start docker
```

Now you'll need the base mariadb docker image:

```
docker pull mariadb
```

Make sure to have the latest images with:

```
docker compose build
```

And then, up the services with:

```
docker compose up
```

If you have a mariadb client installed, you can check the database connection with:

```
mariadb -h 127.0.0.1 -P 3306 -u root -pmulti
```

You can also test the connection to the API via browser with the url <http://127.0.0.1:8000> and the Flask web page with url <http://127.0.0.1:5000>.
