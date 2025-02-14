# fairBnB

fairbnb/
│── app/
│   ├── controllers/                # Presentation Layer (API)
│   │   ├── user_controller.py
│   │   ├── place_controller.py
│   │   ├── review_controller.py
│   │   └── amenity_controller.py
│   │
│   ├── services/                   # Business Logic Layer (Facade)
│   │   ├── user_service.py
│   │   ├── place_service.py
│   │   ├── review_service.py
│   │   └── amenity_service.py
│   │
│   ├── repositories/               # Persistence Layer
│   │   ├── user_repository.py
│   │   ├── place_repository.py
│   │   ├── review_repository.py
│   │   └── amenity_repository.py
│   │
│   ├── models/                     # Database Models
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   │   └── __init__.py
│   │
│   ├── config.py                   # Database Configuration
│   ├── __init__.py
│   ├── routes.py
│
│── run.py                          # Entry Point
│── requirements.txt                # Dependencies
│── README.md
