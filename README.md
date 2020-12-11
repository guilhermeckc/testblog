# DESCRIPTION
###### WAMI: WebApp for Microorganisms Informations
###### WAMI is a webapplication to post informations about microorganisms

# PREREQUISITES
###### Django

# GETTING STARTED ON LINUX
###### Step 1 (Clone this repository): git clone https://github.com/guilhermeckc/testblog.git
###### Step 2 (Create a virtual environment): python3 -m venv venv
###### Step 3 (Activate your environment): source venv/bin/activate
###### Next steps you need execute from your webapp directory:
###### Step 4 (Install dependencies): pip install -r requirements.txt
###### Step 5 (Preparing changes to your model): python manage.py migrate 
###### Step 6 (Creating your model: python manage.py makemigrations blog 
###### Step 7 (Applying changes to your model): python manage.py migrate blog 
###### Step 8 (Create a superuser): python manage.py createsuperuser
###### Step 9 (Run your app!): python manage.py runserver
###### Next steps you need execute from your browser: 
###### Step 10 (Run your webapp): http://127.0.0.1:8000/
###### Step 11 (Create your first post): http://127.0.0.1:8000/admin/
