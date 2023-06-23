# first_rep
It is just a prototype for ecommerse website which is made using django_framework,Bootstrap.This project contains asgi specifications
in order to create seperate chat/comment spaces for each products added by user.Celery is used in this project in order to send mails to each user
after they have signned in.Celerybeat is used in this project to schedule the mails for certain periods of time.Default django database is used to store
all the comments,Celeryworker tasks,Users,User details,User Contacts,CeleryBeat tables.Redis is used as message broker between djangoapp and celeryworker.
There are still lot's of things that need to be configured in this project.
