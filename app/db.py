import json
import docker
docker_client = docker.from_env()

from . import BASEDIR

def create_user(name, password):

    CURRENT_USER_NUM = get_user_amount()
    CURRENT_PORT = f"10{CURRENT_USER_NUM}"

    docker_client.images.build(path=f"{BASEDIR}/app",
        tag=f"{name.lower()}-cloud-img",
        rm=True,
        buildargs={"USER": name, "PASS": password}
        )

    docker_client.containers.run(f"{name.lower()}-cloud-img",
        detach=True, 
        name=f"{name}-cloud", 
        ports={'22/tcp': f'{CURRENT_PORT}22', '80/tcp': f'{CURRENT_PORT}80'}, 
        )

    update_user_amount()
    return CURRENT_PORT

def get_user_amount():

    with open("status.conf", 'r+') as conf:

        data = json.load(conf)
        return data["Users"]

def update_user_amount():

    data = []

    with open("status.conf", 'r+') as conf:

        data = json.load(conf)

    with open("status.conf", 'w+') as conf:

        data["Users"] += 1
        conf.write(json.dumps(data))