# walkmate
Group Project for EECS341

## To make it all work

### Run a postgres instance

```docker run -e POSTGRES_PASSWORD=secretPassword -p:5432:5432 postgres:9.6```

### Build walkmate into a Docker container

```docker build -t buckbaskin/walkmate .```

### Then run the web server from the docker container

```docker run -p 48000:5000 buckbaskin/walkmate python src/runserver.py```