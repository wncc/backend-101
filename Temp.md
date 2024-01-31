First, open your terminal and create a new virtual environment. 
```shell
# Create a new virtual environment
python -m venv venv
```
Then, activate the virtual environment. Note that the command for this depends on your OS. 
```shell
# Activate the virtual environment
./venv/Scripts/Activate.ps1 # Windows
source ./venv/bin/activate # Linux/MacOS
```
Now, install Django using `pip`.
```shell
# Install Django
pip install Django
```
Finally, make a new Django project and try running it.
```shell
# Start a new Django project
django-admin startproject testapp
# Open the project folder
cd testapp
# Run your project 
python manage.py runserver
```
Going to [localhost:8000](http://localhost:8000)
![image](https://github.com/wncc/backend-101/assets/112401585/ea1af057-c50b-4286-94c9-85d28d3e7966)

View Django Installation Page

Explain migrations and migrate

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

Enter username

press enter for email address

enter any password
again password
y and enter


django admin login 


install sqlite viewer


view auth_user in sqlite viewer

python manage.py startapp myapp


in models.py create a model for item

pip install djangorestframework



