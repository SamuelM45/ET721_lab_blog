
# Blog Project

This is a Django-based blog application that allows users to create, read, update, and delete blog posts. The project demonstrates basic Django features such as models, views, templates, forms, and URL routing.

## Prerequisites

Before starting, ensure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Set Up a Virtual Environment

If you're using a Codespace or your local machine, create and activate a virtual environment:

```bash
# Create a virtual environment
python3 -m venv myVirtual

# Activate the virtual environment
source myVirtual/bin/activate
```

### 3. Install Dependencies

Upgrade pip and install Django:

```bash
pip install --upgrade pip
pip install Django
```

### 4. Create the Django Project

Run the following command to create the project structure:

```bash
django-admin startproject blogproject .
```

### 5. Apply Initial Migrations

Set up the database by applying Django’s built-in migrations:

```bash
python manage.py migrate
```

### 6. Create the Blog App

Run the following command to create the `blog` app:

```bash
django-admin startapp blog
```

### 7. Register the Blog App

Add `'blog'` to the `INSTALLED_APPS` list in `blogproject/settings.py`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # Add this line
]
```

### 8. Define the BlogPost Model

Navigate to `blog/models.py` and define the `BlogPost` model:

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

Run the following commands to create and apply the migration for the `BlogPost` model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Create Views and Templates

Define views in `blog/views.py` and create corresponding templates in `blog/templates/blog/`. Refer to the provided code in the project files.

### 10. Configure URLs

Set up URL patterns in `blog/urls.py` and include them in the main project’s `urls.py`.

### 11. Create Forms

Use Django’s `ModelForm` to simplify the creation and editing of blog posts. Define the form in `blog/forms.py`.

### 12. Add Styling

Create a CSS file at `blog/static/blog/styles.css` and link it in `base.html` using Django's static files framework.

### 13. Start the Development Server

Run the server to see your app in action:

```bash
python manage.py runserver
```

Access the app at `http://127.0.0.1:8000/`.

---

## Features

- View a list of all blog posts.
- Create, edit, and delete blog posts.
- View detailed information about a single blog post.
- Responsive design with basic CSS styling.

---

## Folder Structure

```
blogproject/
    blog/
        migrations/
        static/
            blog/
                styles.css
        templates/
            blog/
                base.html
                post_list.html
                post_detail.html
                post_form.html
        admin.py
        apps.py
        forms.py
        models.py
        urls.py
        views.py
    blogproject/
        settings.py
        urls.py
        wsgi.py
    manage.py
```

---

## Contributing

Contributions are welcome! Please create a pull request with your changes.

## License

This project is licensed under the MIT License.



