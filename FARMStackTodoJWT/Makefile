SHELL := /bin/bash


.PHONY: up
up:
	@echo 'starting FARMStackTodoJWT in Docker...'
	docker-compose --env-file ./backend/app/.env.example up --build
