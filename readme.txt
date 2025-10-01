Project: Learning Log

This is a Django-based web application called Learning Log that allows users to create and manage topics and entries related to what they are learning.

Features:
- User registration and login
- Users can create new topics.
- Users can add new entries for each topic.
- Users can edit their existing entries.
- Each user's topics and entries are private.

To run this project:
1. Make sure you have Python and pip installed.
2. Create and activate a virtual environment:
   python -m venv ll_env
   ll_env\Scripts\activate
3. Install the required packages:
   pip install -r requirements.txt
4. Run the database migrations:
   python manage.py migrate
5. Start the development server:
   python manage.py runserver
6. Open your web browser and go to http://127.0.0.1:8000/