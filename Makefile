up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

restart: down up

ssh:
	docker-compose exec robot /bin/bash

on: up ssh