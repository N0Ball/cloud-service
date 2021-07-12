import os
BASEDIR = os.getcwd()

import docker
docker_client = docker.from_env()