import json
import docker
docker_client = docker.from_env()

from app import BASEDIR

def create_user(name, password):

    CURRENT_USER_NUM = get_user_amount()
    CURRENT_PORT = f"{str(CURRENT_USER_NUM).rjust(4, '0')}"

    print(f"Binding Port: {CURRENT_PORT}")

    docker_client.images.build(path=f"{BASEDIR}/app/templates",
        tag=f"{name.lower()}-cloud-img",
        rm=True,
        nocache=True,
        buildargs={"USER": name, "PASS": password}
        )

    docker_client.containers.run(f"{name.lower()}-cloud-img",
        detach=True, 
        name=f"{name}-cloud", 
        volumes={
            f'cloud': {'bind': f'/home/{name}', 'mode': 'rw'}
        },
        ports={'80/tcp': f'2{CURRENT_PORT}', '22/tcp': f'1{CURRENT_PORT}'}, 
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