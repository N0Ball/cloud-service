FROM ubuntu

ARG USER
ARG PASS

RUN apt-get update && apt-get install -y sudo openssl openssh-server

RUN mkdir /var/run/sshd
RUN useradd -rm -d /home/${USER} -s /bin/bash -G sudo -p "$(openssl passwd -1 ${PASS})" ${USER}

EXPOSE 22
CMD [ "/usr/sbin/sshd", "-D" ]