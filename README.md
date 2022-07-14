## Employee Management


## To Run this Project follow below:
```bash
#1.Git Clone Project
$git clone <url>
#2. Creat Virtual Env Or Activate

$mkvirtualenv test
$Workon test

or 

For creating new environment:
$ py -m venv test

To activate your virtual environment:
$ .\test\Scripts\activate

#3. install prerequirement
$ pip install -r requirements.txt

#4. Migrate data
$ python manage.py makemigrations
$ python manage.py migrate

#5. Satrt Development Server
$ python manage.py runserver
```

#### There is a File "DjangoAuthAPI.postman_collection" which has Postman Collection You can import this file in your postman to test this API

