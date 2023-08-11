# start by pulling the python image
FROM python:3.10 as app
LABEL maintainer="Nitin Namdev itsmyidbro@gmail.com"

WORKDIR /fusion

ARG UID=1000
ARG GID=1000

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean \
    && groupadd -g "${GID}" python \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
    && chown python:python -R /fusion

USER python

#copt the requirement file
COPY --chown=python:python requirements*.txt  ./
COPY --chown=python:python bin/* ./bin/

# install the pip3 reqirement using shell script
RUN chmod 0755 bin/* && bash bin/pip3-install

ARG FLASK_DEBUG="false"

#set the environment variable
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_APP="manage.py" \
    PYTHON_PATH="." \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python . .

#exposing the port 5000
EXPOSE 5000

CMD ["gunicorn", "-c", "python:app.common.gunicorn_config", "app.app:create_app('dev')"]
