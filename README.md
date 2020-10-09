# UserActivity
Users and Activity Periods Records API

Go to terminal and create viAPI to serve that data in the json formatrtual env virtualenv .env then active env.
source .env/bin/activate
go into project and install pip requirement txt
pip install -r requirement.txt
Hit the command for Django - 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
API to serve that data in the json format - 
    URL - http://127.0.0.1:8000/demo/
Command will load data from FIXTURE(db.json) to database - 
    python manage.py load_dummy_data_In_Db
Command will load data from database to FIXTURE(db.json) - 
    python manage.py load_dummy_data
