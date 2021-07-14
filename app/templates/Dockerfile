FROM cloud-base

ARG USER
ARG PASS

RUN useradd -rm -d /home/${USER} -s /bin/bash -G sudo -p "$(openssl passwd -1 ${PASS})" -u 1001 ${USER}

WORKDIR /home/${USER}
COPY web ./web
RUN rm -r /var/www/html && ln -s /home/${USER}/web /var/www/html
RUN chown -R ${USER} /home/${USER}/web

VOLUME [ "/home/${USER}" ]

EXPOSE 80 20

ENTRYPOINT [ "sudo", "/bin/bash", "-c", "service apache2 start && /usr/sbin/sshd -D;" ]