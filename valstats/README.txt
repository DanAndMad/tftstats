1. Make sure you are in a python environment and have django restframework installed -> pip install django djangorestframework
2. cd into frontend and install the project dependencies -> cd valstats/frontend -> npm install
3. To run the django server you must be in the valstats subdirectory -> valstats/valstats -> python ./manage.py runserver
4. To run webpack you must be in the frontend subdirectory -> valstats/frontend -> npm run dev
5. Whenever you make a change to a model you must perform a migration -> python ./manage.py makemigrations -> python ./manage.py migrate
