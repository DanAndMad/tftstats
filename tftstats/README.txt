1. Make sure you are in a python environment and have django restframework installed -> pip install django djangorestframework
   Also, have dotenv installed -> pip install python-dotenv
2. cd into frontend and install the project dependencies -> cd tftstats/frontend -> npm install
3. To run the django server you must be in the tftstats subdirectory -> tftstats/tftstats -> python ./manage.py runserver
4. To run webpack you must be in the frontend subdirectory -> tftstats/frontend -> npm run dev
5. Whenever you make a change to a model or pull from a branch you must perform a migration -> python ./manage.py makemigrations -> python ./manage.py migrate
