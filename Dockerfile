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

COPY --chown=python:python requirements*.txt  ./
COPY --chown=python:python bin/* ./bin/

RUN chmod 0755 bin/* && bash bin/pip3-install

ARG FLASK_DEBUG="false"
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_APP="manage.py" \
    PYTHON_PATH="." \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python . .

EXPOSE 5000

CMD ["gunicorn", "-c", "python:app.common.gunicorn_config", "\"app.app:create_app('dev')\""]
# CMD [ "flask", "run" ]

# EXPOSE 5000

# RUN apt-get update && apt-get install -y apache2 apache2-dev libapache2-mod-wsgi-py3 libgl1-mesa-glx 

# COPY . .

# RUN pip3 install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["python"]

# CMD ["manage.py"]
