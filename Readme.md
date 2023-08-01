# Xfusion

install the required packages using pipenv and run the app

``` bash
git clone https://github.com/Vortexdude/Xfusion
cd Xfusion
sudo apt update -y && apt upgrade -y
sudo apt install python3 python3-pip  -y
sudo apt install apache2 apache2-dev libapache2-mod-wsgi-py3 libgl1-mesa-glx -y
pip3 install pipenv
pipenv shell
pipenv install -r requirements.txt
flask run --host=0.0.0.0

```

Visit http://127.0.0.1:5000/swagger-ui
or 
Visit http://<Your-Ip>:5000/swagger-ui

#### Sample 

![Sample screenshot](./sample.png)
