build: 
	docker build . -t cloud-base &&\
	docker network create -d bridge cloud-service-network

clean:
	docker ps -a -q | xargs docker rm -f && \
	yes | docker image prune