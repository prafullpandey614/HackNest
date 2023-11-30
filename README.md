# Hackathon Hosting Application

This Hackathon Hosting Application is built using Django, designed to streamline the process of organizing and managing hackathons.

## Features

- **User Authentication**: Secure login and registration system for participants, organizers, and admins.
- **Hackathon Creation**: Create and manage hackathons with details on dates, themes, and rules.
- **Team Formation**: Facilitate team creation, joining, and management for participants.
- **Project Submission**: Allow participants to submit their projects with descriptions and links.
- **Judging System**: Implement a judging system for evaluating projects.
- **Admin Dashboard**: Centralized dashboard for admins to oversee and manage hackathons and users.
- **Email Notifications**: Automated emails for updates, reminders, and notifications.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/hackathon-app.git
   ```
2. Create a Virtual Environment:
   ```bash
   python -m venv env
   ```
3. Install Dependencies and Requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run Migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Start the Server
    ```bash
    python manage.py runserver
    ```


