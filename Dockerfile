# start by pulling the python image
FROM python:3.10 as app
LABEL maintainer="Nitin Namdev itsmyidbro@gmail.com"

WORKDIR /fusion


RUN apt-get update -y \
    && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean 

#copt the requirement file
COPY requirements*.txt  ./

RUN pip3 install -r ./requirements.txt

ARG FLASK_DEBUG="false"

#set the environment variable
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_APP="manage.py" \
    PYTHONUNBUFFERED="true" 
    # PATH="${PATH}:/bin:/usr/bin:/usr/local/bin"

COPY . .

#exposing the port 5000
EXPOSE 5000
