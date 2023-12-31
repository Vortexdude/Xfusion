# Makefile for Docker Compose Up and Build

# Name of the project and the Docker Compose service
PROJECT_NAME := myproject

# Command to execute Docker Compose
DOCKER_COMPOSE := docker-compose
DOCKER_VOLUME := docker volume
DOCKER_SYSTEM := docker system

.PHONY: build up down sRemove vRemove

# Target to build the Docker Compose services
build:
	$(DOCKER_COMPOSE) build

# Target to bring up the Docker Compose services
up:
	$(DOCKER_COMPOSE) up

# Target to bring down the Docker Compose services
down:
	$(DOCKER_COMPOSE) down

sRemove:
	$(DOCKER_SYSTEM) prune -f

vRemove:
	$(DOCKER_VOLUME) prune -f


# Target to build and then bring up the services
run: build up

# Target to stop the services
stop: down

# Target to restart the services
restart: stop up

delete: sRemove vRemove

# Target to build, bring up, and then connect to a shell in a service
connect: build up
	$(DOCKER_COMPOSE) exec <service-name> /bin/bash
