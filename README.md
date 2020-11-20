# Simple Flask application using Docker and docker-compose

This small project demos use of the Flask framework with Jinja2 templates together with Docker / docker-compose for web development. It uses Gunicorn as an application server and NGINX as a proxy. Files are mounted in the container and both templates and the app.py will be reloaded automatically within the container when changed locally.

## Installation

```
# git clone https://github.com/Kungbib/flask-docker-example
# cd flask-docker-example
```

## Run

The following will build and deploy the container locally.

```
# docker-compose up
```

Add the `-d` parameter to run in background.

## Test

Test that the container is running by executing `docker-compose ps`. Check output logs with `docker-compose logs`. To continually monitor output run `docker-compose logs --tail 100 -f`.

Go to http://localhost:8080/ or run `curl http://localhost:8080`. To test the template engine add parameter `use_template` to the URL.

