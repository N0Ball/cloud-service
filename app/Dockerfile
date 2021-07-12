FROM cloud-base

ARG USER
ARG PASS

RUN useradd -rm -d /home/${USER} -s /bin/bash -G sudo -p "$(openssl passwd -1 ${PASS})" -u 1001 ${USER}
EXPOSE 22 80

CMD [ "sudo", "/bin/bash", "-c", "service apache2 start; /usr/sbin/sshd -D" ]