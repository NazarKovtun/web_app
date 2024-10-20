# Web App

## Description
This web application is implemented using Django and provides basic functionality 
for managing articles: adding, editing, deleting, and viewing. It serves as a template 
for personal blogs or small news websites.

Users can publish their own articles and explore others, enabling them to share valuable information.

This project serves as a basic example for developing similar applications. While working on it, I learned to:
- **Create** projects using Django;
- **Write** web pages using HTML and CSS;
- **Interact** with the database using Django ORM.


## Features
This platform allows for posting and reading articles on any topic.

**Key functionalities:**
- **Create articles:** Users can add new articles;
- **Edit articles:** Users can update existing articles;
- **Delete articles:** Users can remove articles;
- **View articles:** Users can browse a list of articles and view details of individual articles.


## How to Run the Project
**To get started, follow these steps:**

1. **Clone repository:**
```bash
git clone https://github.com/NazarKovtun/web_app.git
cd web_app
```

2. **Installing the requirements:**
```bash
pip install -r 'requirements.txt'
```

3. **Apply database migrations:**
```bash
python manage.py migrate
```

4. **Start the local server:**
```bash
python manage.py runserver
```

![Runserver](web_app/my_site/img/runserver.png)

5. **Open the web app in your browser:**

Navigate to `http://127.0.0.1:8000/` to view the home page.

![Main_page](web_app/my_site/img/main_page.png)

## What's inside
- `/main` contais the main settings for the application;
- `/my_site` handle the home page functionality;
- `/news` manage the news page.


## Requirements
- Django 5.0.7
- Python 3.11
