FROM ubuntu

RUN apt-get update && apt-get install -y sudo openssl openssh-server
RUN apt-get install -y apache2

RUN mkdir /run/sshd