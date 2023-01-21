SHELL := /bin/bash


.PHONY: up
up:
	@echo 'starting DRFPostgresReactNotes in Docker...'
	chmod +x mysite1/entrypoint.sh
	docker-compose --env-file ./.env.example up --build

.PHONY: clean
clean:
	@echo 'Removing volumes along with the containers for DRFPostgresReactNotes...'
	docker-compose down -v
