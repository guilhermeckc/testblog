# DESCRIPTION
**WAMI**: **W**eb**A**pp for **M**icroorganisms **I**nformations

WAMI is a webapplication to post and view informations about microorganisms

# PREREQUISITES
Django

# GETTING STARTED ON LINUX
1. Clone this repository: ```git clone https://github.com/guilhermeckc/testblog.git```
2. Create a virtual environment: ```python3 -m venv venv```
3. Activate your environment: ```source venv/bin/activate```

#### Next steps you need execute from your webapp directory:
4. Install dependencies: ```pip install -r requirements.txt```
5. Preparing changes to your model: ```python manage.py migrate ```
6. Creating your model: ```python manage.py makemigrations blog```
7. Applying changes to your model: ```python manage.py migrate blog``` 
8. Create a superuser: ```python manage.py createsuperuser```
9. Run your app: ```python manage.py runserver```

#### Next steps you need execute from your browser:
10. Open your webapp: ```http://127.0.0.1:8000/```
11. Create your first post: ```http://127.0.0.1:8000/admin/```
