# auth-api

To use this project you need to have all the packages that are mentioned in requirements.txt and postgres and pgadmin installed.
You can create a virtual environment and install the packages. For that

create an environment:
conda create -n venv python=3.7.6 anaconda

activate the environment:
conda activate venv

once you activate the environment install all packages mentioned in requirements.txt

Setting the project:

1. To start the project clone the repository. Once you are done you will see a directory by name auth-api.

2. Enter into directory using command cd auth-api. 

3. Now activate the environment that you created earlier using the command:  conda activate venv

4. Now open myapi/settings.py file and change the user name and password according to your own postgresql creadentials.

......
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myapi',
        'USER': 'postgres', #change to your user name
        'PASSWORD': '1234', #change it to your password
        'HOST': 'localhost',
    }
}
......

5. open pgadmin and create a database "myapi".

6. Now to properly create tables we need to alter authpp/migrations. This can be done as follows
       a. python manage.py migrate --fake authapp zero
       b. python rm -rf migrations
       c. python manage.py makemigrations authapp
       d. manage.py migrate --fake authapp

7. Create a super user to access admin panel using the command
        python manage.py createsuperuser

8. Done!!!. Now you are ready to run the server using the command 
        python manage.py runserver

