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
$ flask run
```
*   Run Flask in debug mode
```sh
$ export FLASK_ENV=development
$ flask run
```

### Docker setup & installation:
*   Build docker image using Dockerfile
```sh
$ docker build -t <DOCKER IMAGE> .
```
*   Run container
```sh
$ docker run -d --name <CONTAINER NAME> -p 5000:5000 <DOCKER IMAGE>
```

## Testing
*   On local machine
```sh
$ pytest
```
*   Inside docker container
```sh
$ docker exec <CONTAINER NAME> pytest 
```


