include .env
export

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

restart: down up

ssh:
	docker-compose exec robot /bin/bash

on: up ssh

sync:
    rsync . pi@${PI_HOST}:ros2_walkaround --dry-run --exclude='/.git' --filter="dir-merge,- .gitignore"