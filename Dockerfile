# start by pulling the python image
FROM python:3.10
EXPOSE 5000

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# Install Apache and mod_wsgi using apt-get
RUN apt-get update && apt-get install -y apache2 apache2-dev libapache2-mod-wsgi-py3 libgl1-mesa-glx 

# Copy the Pipfiles to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# install the dependencies and packages in the requirements file
RUN pipenv install --deploy --ignore-pipfile
# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
# ENTRYPOINT ["python"]

CMD ["python", "-m", "flask", "run"]
