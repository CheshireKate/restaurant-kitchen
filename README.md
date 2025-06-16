# Restaurant Kitchen Service

A web-based kitchen management system built with Django. Designed to streamline restaurant kitchen operations by managing dishes, cooks, and more.

## Features

* Manage cooks and dishes
* Admin interface with Django
* Bootstrap 5 + Crispy Forms integration for better UI
* Ready for testing with `pytest`
* Modular design using Django apps

## Requirements

```
Django~=4.1  
asgiref~=3.8.1  
sqlparse~=0.5.2  
bootstrap5  
crispy_forms  
attrs~=24.2.0  
pytest~=7.1.3  
packaging~=24.1  
pip~=23.2.1  
```

Install with:

```bash
pip install -r requirements.txt
```

## 🏁 Getting Started

1. **Clone the repo:**

   ```bash
   git clone https://your.repo.url/restaurant-kitchen-service.git
   cd restaurant-kitchen-service
   ```

2. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

4. **Access the app:**
   Open [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with your superuser account.

## Running Tests

```bash
pytest
```

## 🗃️ Project Structure (simplified)

```
restaurant-kitchen-service/
├── manage.py
├── restaurant/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── cooks/
├── dishes/
├── customers/
└── requirements.txt
```

## Tech Stack

* Python
* Django
* Bootstrap 5
* SQLite (default)

##  Notes

* This project is set up for development (`DEBUG = True`).
* The admin panel is your main interface unless custom views are added.

## Render Link
   https://restaurant-e3t9.onrender.com

