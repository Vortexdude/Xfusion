FROM python:3.10
EXPOSE 5000
WORKDIR /Xfusion
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "run.py"]
