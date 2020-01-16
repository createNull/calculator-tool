# Calculator Tool

Web application developed in Flask and deployed with Docker in Heroku.
The purpose of this app is to provide a calculator tool for simple algorithms using some input from user.
In case of valid input, the result of the algorithm together with its execution time in seconds will be displayed.
Otherwise, an error message will pop-up.

## Prerequisites:
*   Python 3.x
*   Docker
*   Heroku


### Local setup & installation:
*   Create and activate [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
*   Install project requirements using pip
```
pip install -r requirements.txt
```
*   Run application:
```
python app/server.py
```
*   Run tests (coverage + reporting)
```
pytest
```

### Docker setup & installation:
*   Build docker image using Dockerfile
```
docker build -t <DOCKER_IMAGE> .
```
*   Run app
```
docker run -d --name <CONTAINER_NAME> -p 5000:5000 <DOCKER_IMAGE>
```
*   Run tests (coverage + reporting)
```
docker exec <CONTAINER_NAME> pytest 
```
*   Stop & remove container
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/createNull/calculator-tool)


## License

The mighty MIT license. Please check `LICENSE` for more details.
