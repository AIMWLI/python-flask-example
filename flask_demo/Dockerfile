FROM bitnami/python:3.12.3-debian-12-r11

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG production

RUN sed -i 's|security.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list
RUN sed -i 's|deb.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list


RUN adduser flasky
# RUN adduser -D flasky
USER flasky

WORKDIR /home/flasky

COPY requirements requirements
# 如果没有venv: sudo apt-get install python3-venv
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY flasky.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
