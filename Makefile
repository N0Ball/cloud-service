build:
	docker build . -t cloud-base

clean:
	docker ps -a -q | xargs docker rm -f && \
	yes | docker image prune