# Xfusion

install the required packages using pipenv and run the app

``` bash
sudo apt install python3 python3-pip 
sudo apt install apache2 apache2-dev libapache2-mod-wsgi-py3 libgl1-mesa-glx
pip3 install pipenv
pipenv shell
pipenv install -r requirements.txt
flask run --host=0.0.0.0

```

Visit http://127.0.0.1:5000
or 
Visit http://<Your-Ip>:5000

#### Sample 

![Sample screenshot](./sample.png)
