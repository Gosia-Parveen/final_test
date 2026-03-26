#  A_Certificates – Certificate Generation System

This is a Django-based web application designed to manage events, participants, and automatically generate certificates.
The system allows an admin to create events, add participants, and generate certificates, while users can log in to view 
their participation details and download their certificates.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Features

* Admin Dashboard

  * Add Events
  * Add Participants
  * Generate Certificates

* User Dashboard

  * View participated events
  * View certificates
  * Download certificates

* Authentication System

  * Separate admin and user login
  * Data filtered based on user email

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Tech Stack

* Python
* Django
* SQLite (default database)
* HTML, CSS, Bootstrap

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Setup Instructions

Follow these steps to run the project on your system:

### 1. Clone the repository

git clone <>

cd <A_Certificates>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2. Install dependencies

  pip install django
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 3. Apply migrations

  python manage.py makemigrations
  
  python manage.py migrate
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 4. Create superuser (admin)

  python manage.py createsuperuser
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 5. Run the server

  python manage.py runserver

  Open in browser:

   http://127.0.0.1:8000/

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  How the System Works

1. Admin logs in and creates events
2. Admin adds participants using their email
3. User logs in using same email
4. User can see:

   * Events they participated in
   * Certificates generated for them
   * Can easily download the certificates as well

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Important Note

The system links users and participants using email.


So make sure:
  
  User email == Participant email

  Otherwise, data will not be visible on the user dashboard.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Demo Video 

Watch the working of the project here:
  **https://drive.google.com/file/d/13lLZ04MIVs9A8kyFPIYDkT3eMIN1hVMh/view?usp=sharing

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Author

Developed by a student as a full-stack Django project to understand real-world workflow and backend logic.
