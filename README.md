# auto-stundenprotokoll
Enabling teachers of the German BuT to automate their protocols

[Usage under OS X](##OS X)

[Usage under Linux](##Linux)

##OS X

1. Install git by typing git into the terminal. If you don't have it installed yet you'll be prompted to install the command line tools. Follow the instructions.

2. Pull the repository `git clone git@github.com:wolfskaempf/auto-stundenprotokoll.git`

3. Change into the new directory `cd auto-stundenprotokoll`

4. Open the virtual environment. `source bin/activate`

5. Initialize the database `python manage.py makemigrations && python manage.py migrate`

6. Create a superuser `python manage.py createsuperuser`

7. Run the server `python manage.py runserver`

8. Open http://127.0.0.1:8000/admin/ inside your browser and log in using the super user data you entered in the fifth step.

9. Create a Class, a Student and one Lesson.

10. Open http://127.0.0.1:8000/

11. You're done.

##Linux

1. Install git `sudo apt-get install git`

2. Pull the repository `git clone git@github.com:wolfskaempf/auto-stundenprotokoll.git`

3. Change into the new directory `cd auto-stundenprotokoll`

4. Open the virtual environment. `source bin/activate`

5. Initialize the database `python manage.py makemigrations && python manage.py migrate`

6. Create a superuser `python manage.py createsuperuser`

7. Run the server `python manage.py runserver`

8. Open http://127.0.0.1:8000/admin/ inside your browser and log in using the super user data you entered in the fifth step.

9. Create a Class, a Student and one Lesson.

10. Open http://127.0.0.1:8000/

11. You're done.
