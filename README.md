# bruteforce-app
app for bruteforce simulation and sandboxing

Naming Convention 
feature/feature-name
bugfix/bug-description
hotfix/critical-bug


#strucutre 
my-python-app/
│
├── app/                     # Main application code
│   ├── __init__.py
│   ├── models.py            # Database models
│   ├── routes.py            # API routes
│   ├── services.py          # Business logic
│   ├── static/              # Static files (CSS, JS, images)
│   └── templates/           # HTML templates (if using Flask/Django)
│
├── tests/                   # Unit and integration tests
│   ├── test_routes.py
│   └── test_models.py
│
├── venv/                    # Virtual environment (ignored by `.gitignore`)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (ignored by `.gitignore`)
├── .env.example             # Sample environment variables
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation



