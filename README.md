# auto-stundenprotokoll [![Code Issues](https://www.quantifiedcode.com/api/v1/project/1632c04beb9d4b9c8e5c106bce1cc395/badge.svg)](https://www.quantifiedcode.com/app/project/1632c04beb9d4b9c8e5c106bce1cc395)
Enabling teachers of the German BuT to automate their protocols

You can find usage information for OS X and Linux below. Windows should also work but some commands are entirely different.

##OS X and Linux

1. Install git by typing git into the terminal. If you don't have it installed yet you'll be prompted to install the command line tools. Follow the instructions.

2. Pull the repository `git clone https://github.com/wolfskaempf/auto-stundenprotokoll.git`

3. Change into the new directory `cd auto-stundenprotokoll`

4. Create a virtual environment `virtualenv .`

4. Open the virtual environment. `source bin/activate`

4. Install all necessary components `pip install -r requirements.txt`

5. Initialize the database `python manage.py migrate`

6. Create a superuser `python manage.py createsuperuser`

7. Run the server `python manage.py runserver`

8. Open http://127.0.0.1:8000/admin/ inside your browser and log in using the super user data you entered previously.

9. Create a Class, at least one Student and at least at least one Lesson.

10. Open http://127.0.0.1:8000/ and print your protocols.

11. You're done.
