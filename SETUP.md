# Employee Manger Setup Guide

This guide will assist you in setting up a project that uses Django and Vue.

## Prerequisites

Ensure the following are installed on your system:
- Python 3.7 or higher
- Node.js 20.0 or higher
- pip (Python package installer)
- npm (Node package manager)

## Steps to Setup Backend

### Create Virtual Environment

``` bash linux
python3 -m venv .env
```

``` bash windows
py -m venv .env
```

### Activate Virtual Environment

``` bash linux
.env/bin/activate
```

``` bash windows
.env/scripts/activate
```

### Navigate to the 'backend' Directory

``` bash
cd backend
```

### Install Necessary Dependencies Listed in the 'requirements.txt' File

``` bash
pip install -r requirements.txt
```

### Create and configure django .env file from .env_template

``` bash
cp .env_template .env
```

Edit variables to match your environment:
SECRET_KEY=1234
CORS_ALLOWED_ORIGINS=http://127.0.0.1:8080 http://localhost:8080
ALLOWED_HOSTS=localhost
DEBUG=true

### Migrate the Database

``` bash
python manage.py migrate
```

### Seed Database - Optional

``` bash
python manage.py seed
```

### Steps to Run the Backend Server

``` bash
python manage.py runserver
```

## Steps to Setup Frontend

``` bash
cd frontend
npm i
```

### Create and configure vue .env file from .env_template

``` bash
cp .env_template .env
```

Add the following to .env file matching your local environment:
VUE_APP_BASE_URL=http://localhost:8000
as an example

### Steps to Run the Frontend Server

``` bash
npm run serve
```

## Steps to Build the Frontend

``` bash
cd frontend
npm run build
```
