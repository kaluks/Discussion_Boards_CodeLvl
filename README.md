This is my capstone project for Code Louisville's python course. I created a message board app with the goal of learning User Authentications & Authorizations via login accounts.

As resources, I used the tutorial Simple Is Better Than Complex, Treehouse Python & Django courses, and DjangoGirls.org.


To run this on your local machine:
Clone the repository to your local machine:
https://github.com/kaluks/Discussion_Boards_CodeLvl.git


Install the requirements:
cd to the directory that contains requirements.txt (probably Discussion_Boards_CodeLvl/), then

pip install -r requirements.txt


Create the database:

python manage.py migrate


Run the development server:

python manage.py runserver

view in your browser at  127.0.0.1:8000
