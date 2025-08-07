# 🎶 MusicPlanner – Practice Planner for Self-Taught Musicians

A web application that helps self-taught musicians set musical goals, generate personalized practice plans, track daily/weekly progress, and receive improvement suggestions based on their performance.

---

## 🚀 Technologies

- Python 3.10+
- Django 5
- Django REST Framework
- SQLite (for development)
- JWT (authentication)
- python-decouple (environment variable management)
- Postman (for testing)

---

## 📁 Project Structure

musicplanner/
├── config/               # Global Django configuration
│   └── settings.py
├── users/                # Custom user app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── .env

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/your-username/musicplanner.git
cd musicplanner

### 2. Create a virtual environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

If requirements.txt is missing, install manually:

pip install django djangorestframework python-decouple

### 4. Configure environment variables

Create a .env file in the project root with:

SECRET_KEY="your_super_secret_key"
DEBUG=True

### 5. Apply migrations

python manage.py makemigrations
python manage.py migrate

### 6. Run the development server

python manage.py runserver

---

## 🔐 Available Endpoints

### 📍 Test Route  
GET /api/users/  
Response:  
{"message": "Users API is working"}

### 📝 User Registration  
POST /api/users/register/  
JSON Body:  
{
  "email": "user@example.com",
  "username": "your_username",
  "password": "secure_password"
}

---

## 🧩 Next Steps

- Implement JWT authentication  
- Create musical profiles and goals  
- Generate practice plans  
- Build progress tracking  
- Complete backend ready for frontend connection

---

## 📄 License

MIT © 2025 Johana Amorín
