# week4_project

Application to manage book-reading events, in a geographical location with single timezone. Details needed from the API:
    
    1.New users can login/signup.
    2.Users can create events and invite other existing users.
    3.Events can be public or private (only invited users can attend/view) events.
    4.User can view all the events, but past events are shown differently.
    5.User can filter all events, they are invited to(private events).
    6.User can filter the events  with filter(private, public, ongoing, past, upcoming).
    7.User can edit an event. 
    8.Users can delete the events created by them, (conditional delete: only future events).
    9.Admin user can view or filter or  edit /delete  any events.

    
    
Deployed GET, POST, PATCH and DELETE API's to handle all the cases required.



The first thing to do is to clone the repository:

        $ git clone https://github.com/pandemic07/week4_project.git
Create a virtual environment to install dependencies in and activate it:

         $ pip install virtualenv
         $ virtalenv env_name
         $ source path/bin/activate  like source /home/your_name/Environments/env_name/bin/activate
Then install the dependencies:

        (env)$ pip install -r requirements.txt
Once pip has finished downloading the dependencies:

        (env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000

Now you can see the link for Employee and Devices and perform CRUD operations
