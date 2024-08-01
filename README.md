# Student Task Tracker in Django


## How To Setup
```
git clone https://github.com/admingrey/studydownunder.git
```
```
cd studenttasktracker
extract the static/static.rar to the folder static/
rename "dot_env" file to ".env"
then change the settings according to your mysql setup:

SECRET_KEY="your django secret key"
DATABASE_NAME=studenttasktracker
DATABASE_USER=root
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=3306

```
```
python -m pip install virtualenv
```
```
virtualenv venv
```
```
venv/scripts/activate
```
```
python -m pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
"# SEP_task_tracker-main" 
