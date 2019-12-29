# Calculator Tool
Web server developed in Flask which can be used across different web based applications. This app purpose
is to provide a calculator tool for simple algorithms using input from user. The output will be the result of the algorithm (in case of valid input) or an error message (in case of invalid input). This service also provides the execution time in seconds for each calculation.

## Prerequisites:
*   Python3.x
*   Docker


### Local setup & installation:
*   Create and activate [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
*   Install project requirements using pip
```sh
$ pip install -r requirements.txt
$ cd app
```
*   Run following commands for Flask:
```sh
$ export FLASK_APP=server.py
$ export FLASK_ENV=development (debug mode)
$ flask run
```
*   Run tests
```sh
$ pytest
```

### Docker setup & installation:
*   Build docker image using Dockerfile
```sh
$ docker build -t <DOCKER_IMAGE> .
```
*   Run app
```sh
$ docker run -d --name <CONTAINER_NAME> -p 5000:5000 <DOCKER_IMAGE>
```
*   Run tests
```sh
$ docker exec <CONTAINER_NAME> pytest 
```


