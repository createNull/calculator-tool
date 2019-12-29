# Calculator Tool
Web server developed in Flask which can be used across different web based applications. This app purpose
is to provide a calculator tool for simple algorithms using input from user. The output will be the result of the algorithm in case of valid input. An error message will be shown in case of invalid input. This tool also provides the execution time in seconds for each algorithm.

## Prerequisites:
*   Python3.x
*   Docker


### Local setup & installation:
*   Create and activate [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
*   Install project requirements using pip
```sh
$ pip install -r requirements.txt
```
*   Run application:
```sh
$ python app/server.py
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
*   Stop & remove container
```sh
$ docker stop $(docker ps -a -q)
$ docker rm $(docker ps -a -q)
```

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/createNull/calculator-tool)


## License

The mighty MIT license. Please check `LICENSE` for more details.
