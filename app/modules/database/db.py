import os
import json
import docker
docker_client = docker.from_env()

from app import BASEDIR, APP_DIR

def create_user(name, password):

    CURRENT_USER_NUM = get_user_amount()
    CURRENT_PORT = f"{str(CURRENT_USER_NUM).rjust(4, '0')}"

    try:
        os.makedirs(f"{APP_DIR}/{name}")
    except FileExistsError:
        print("user exist")

    docker_client.images.build(path=f"{BASEDIR}/app/templates",
        tag=f"{name.lower()}-cloud-img",
        rm=True,
        nocache=True,
        buildargs={"USER": name, "PASS": password}
        )

    docker_client.volumes.create(name=f"{name.lower()}-cloud-volume",
        driver="local",
        driver_opts={
            "o" : "bind",
            "type": "none",
            "device": f"{APP_DIR}/{name}"
        },
        )

    port = create_container(name, CURRENT_PORT)

    update_user_amount(port)
    return CURRENT_PORT

def create_container(name, port):
    try:
        docker_client.containers.run(f"{name.lower()}-cloud-img",
        detach=True, 
        name=f"{name}-cloud",
        labels=['cloud-service'],
        volumes={
            f"{name.lower()}-cloud-volume": {'bind': f'/home/{name}', 'mode': 'rw'}
        },
        ports={'80/tcp': f'2{port}', '22/tcp': f'1{port}'}, 
        )
    except docker.errors.APIError:
        print("Trying getting another port")
        return create_container(name, port+1)

    return port




def get_user_amount():

    with open("status.conf", 'r+') as conf:

        data = json.load(conf)
        return data["Users"]

def update_user_amount(port):

    data = []

    with open("status.conf", 'r+') as conf:

        data = json.load(conf)

    with open("status.conf", 'w+') as conf:

        data["Users"] = port
        conf.write(json.dumps(data))