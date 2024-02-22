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

``` bash
python -m venv venv
```

### Activate Virtual Environment

``` bash
.env/bin/activate
```

### Navigate to the 'backend' Directory

``` bash
cd backend
```

### Install Necessary Dependencies Listed in the 'requirements.txt' File

``` bash
pip install -r requirements.txt
```

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
npm install
```

## Frontend Configuration

Add the following to .env file:
VUE_APP_BASE_URL = [http://localhost:8000](http://localhost:8000) as an example

### Steps to Run the Frontend Server

``` bash
npm run serve
```

## Steps to Build the Frontend

``` bash
npm run build
```
