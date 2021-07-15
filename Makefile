#!make
include .env
export $(shell sed 's/=.*//' .env)

test:
	flask test

dev:
	export MODE=DEVELOPMENT
	flask run --reload

restart:
	docker compose down &&\
	make run

run:
	docker compose build --no-cache &&\
	docker compose up -d

build: 
	mkdir -p $(CLOUD_SERVICE_DIR) &&\
	docker build ./app/templates/base -t cloud-base &&\
	echo "{\"Users\": 1}" > status.conf

clean:
	docker compose down &&\
	docker ps -a -q -f "label=cloud-service" | xargs docker rm -f && \
	docker images --format "{{.Repository}}" | grep ".-cloud-img" | xargs docker rmi -f && \
	docker volume ls -q | grep ".*-cloud-volume" | xargs docker volume rm -f && \
	rm -rf $(CLOUD_SERVICE_DIR) && \
	docker image prune -f