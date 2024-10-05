Job Finder Application:
This is a backend-only Django-based job finder application that allows job seekers (users) to register, create profiles, search for jobs, and apply for jobs. Admins can manage job postings and view job applications. The application exposes API endpoints for user authentication, job search, job application, and admin functionalities.

Features:
User Registration & Authentication: Users can register and log in.
Profile Management: Users can create and update their profiles.
Job Search: Users can search for jobs with filters like title, location, and salary.
Job Application: Users can apply for jobs, and their applications are stored and tracked.
Admin/Employer: Admins can create, edit, delete jobs, and view job applications.
Role-based Access Control: Only admins can manage jobs and view applications.

Requirements:
Python 3.x
Django 4.x
Django REST Framework
SQLite (default) or any other database supported by Django

API Endpoints
Register:
POST /api/register/
json
{ "username": "user", "password": "pass" }

Manage Profile:
GET/POST /api/profile/
Headers: Authorization: Token <user-token>

Job Listings:
GET /api/jobs/

Apply for Job:
POST /api/jobs/<job_id>/apply/
Headers: Authorization: Token <user-token>

Admin Job Management (Create/Update/Delete Jobs, View Applications):
Requires Admin Token.

Run Tests
python manage.py test
Tools (Postman/cURL)
Use Postman or cURL to interact with the API. For authenticated routes, provide the Authorization: Token <your-token> header.
