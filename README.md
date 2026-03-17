# DjangoShop

Simple e-commerce backend built with Django.

## Description
**DjangoShop** is a lightweight online store backend developed with Python and Django. The project demonstrates a standard e-commerce architecture, including product management, order processing, and relational data mapping between users and their purchases.

It was created as a learning project to practice backend development, relational database design (SQL), and Django ORM.

---

## Features
* **Product Management:** Full CRUD capabilities via Django Admin.
* **Order System:** User-based order creation and tracking.
* **Order Items:** Support for multiple products within a single order with quantity tracking.
* **Django Admin Integration:** Pre-configured administrative interface for managing the store.
* **Clean Architecture:** Separation of concerns between models, views, and routing.

---

## Tech Stack
* **Language:** Python 3.x
* **Framework:** Django
* **Database:** SQLite (default Django database)
* **ORM:** Django Object-Relational Mapper

---

## Project Structure
```text
DjangoShop/
│
├── shop/               # Core application logic
│   ├── admin.py        # Admin panel configurations
│   ├── models.py       # Database schemas (Product, Order, OrderItem)
│   ├── views.py        # Logic for processing requests
│   └── urls.py         # App-specific routing
│
├── DjangoShop/         # Project settings and configuration
│   ├── settings.py
│   └── urls.py
│
├── manage.py           # Django management utility
└── db.sqlite3          # Local database file
```

# Datamodels 

## Order
### Represents a specific order placed by a user.

* user: Reference to the Django User model.
* created_at: Date and time when the order was placed.
* status: Current status of the order.

# OrderItem

### Links a specific product to an order. 

* order: Reference to the parent Order.
* product: Reference to the Product being purchased.
* quantity: The number of units for this specific product.

## Future Improvements
- [ ] **Shopping cart implementation:** Managing temporary selections using Django sessions.
- [ ] **REST API development:** Building endpoints via Django REST Framework for frontend integration.
- [ ] **Payment gateway integration:** Secure transaction handling with providers like Stripe or PayPal.
- [ ] **Product image support:** Implementing media handling and storage for item visuals.
- [ ] **Advanced filtering and search:** Improved user experience with category, price, and keyword queries.


# Author
### David (Zixther)
### GitHub: Zixtherc