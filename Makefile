.PHONY: start stop test

build:
	docker-compose build

start:
	docker-compose up --build

stop:
	docker-compose down
