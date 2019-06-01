# Lumen Project README

## Prerequisites

Install Docker [here](https://docs.docker.com/v17.12/)

## Development

This project ships with several containers that will help you do things like run your application locally, format and lint your code, and run your projects' test suite.

### Test Container
To run our test suite in a container, use `docker-compose run test`

This will kick off:
- code formatting using `black`
- code linting using `flake8`
- static type analysis using `mypy`
- test suite with `pytest` 

These commands are defined in `docker/run_tests.sh`

This test container attempts to closely mimic the types of tasks that will be run in CI, and should be run prior to pushing code

### Service Container
To run the application locally, use `docker-compose up service`

This will run the flask application on the docker network on port 5000.

> Generally, you can access this on `localhost:5000`.
> However, if you are using Docker Toolbox instead of Docker Engine (I am running Windows Home Edition on my PC, and cannot use Docker Engine), the docker network wont map to your `localhost`.
> It will instead run its own network on a `docker-machine`, which is essentially a virtual host running on Virtual Box. To find this IP, you can run `docker-machine ls`

```bash
Josh@DESKTOP-xxxx MINGW64 ~/Documents/codebase/lumen (master)
$ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER     ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v18.09.6
```

Using the address in the `url` column, we can hit `192.168.99.100:5000` in a web browser to hit our application.
A successful request to the `/` endpoint will return some json to you.

```bash
{
"message": "hello world"
}
```

