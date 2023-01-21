SHELL := /bin/bash


.PHONY: up
up:
	@echo 'starting DRFPostgresReactNotes in Docker...'
	chmod +x backend/entrypoint.sh
	docker-compose --env-file ./.env.example up --build

.PHONY: clean
clean:
	@echo 'Removing volumes along with the containers for DRFPostgresReactNotes...'
	docker-compose down -v
