# DjangoShop

Simple e-commerce backend built with Django.

## Description

DjangoShop is a simple online store backend written with Django.  
The project demonstrates the basic architecture of an e-commerce system including products, orders and order items.

It was created as a learning project to practice backend development with Django, relational databases and application structure.

---

## Features

- Product management
- Order creation
- Order items with quantity
- User-based orders
- Django ORM models
- Django admin support

---

## Tech Stack

- Python
- Django
- SQLite (default Django database)
- Django ORM

---

## Project Structure

```
DjangoShop/
│
├── shop/              # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── DjangoShop/        # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── db.sqlite3
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Zixtherc/DjangoShop.git
cd DjangoShop
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install django
```

---

## Run the Project

Apply migrations:

```bash
python manage.py migrate
```

Run development server:

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## Models

### Order

Represents a user order.

Fields:

- `user` — reference to Django User
- `created_at` — order creation date
- `status` — order status

### OrderItem

Represents a product inside an order.

Fields:

- `order` — reference to Order
- `product` — reference to Product
- `quantity` — number of items

---

## Future Improvements

- Shopping cart
- REST API (Django REST Framework)
- Payment integration
- Product images
- Pagination and filtering
- Authentication improvements

---

## Author

David (Zixther)