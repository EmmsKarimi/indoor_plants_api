Great! Here’s your updated **README.md** with your GitHub link included:

---

# 🌿 Indoor Plants Management System API

This API helps indoor plant owners manage their plants, maintenance tasks, and internal orders. It is built with Django REST Framework and secured with user authentication.

🔗 GitHub Repo: [https://github.com/EmmsKarimi/indoor_plants_api](https://github.com/EmmsKarimi/indoor_plants_api)

---

## 🔑 Features

- User registration & login  
- Add, update, delete, and view plants  
- Schedule and track maintenance tasks  
- Manage internal orders  
- Swagger API documentation

---

## 🛠 Setup

```bash
git clone https://github.com/EmmsKarimi/indoor_plants_api.git
cd indoor_plants_api
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🚀 API Endpoints

### Auth
- `POST /register/` – Register  
- `POST /login/` – Login  
- `GET /profile/` – View profile  
- `PUT /profile/` – Update profile  

### Plants
- `GET /plants/` – List plants  
- `POST /plants/` – Add plant  
- `GET /plants/{id}/` – View plant  
- `PUT /plants/{id}/` – Update plant  
- `DELETE /plants/{id}/` – Delete plant  

### Maintenance
- `GET /maintenance/` – List tasks  
- `POST /maintenance/` – Add task  
- `GET /maintenance/{id}/` – View task  
- `PUT /maintenance/{id}/` – Update task  
- `DELETE /maintenance/{id}/` – Delete task  

### Orders (Internal use only)
- `GET /orders/` – List orders  
- `POST /orders/` – Create order  
- `GET /orders/{id}/` – View order  
- `PUT /orders/{id}/` – Update order  
- `DELETE /orders/{id}/` – Cancel order  

---

## 🧾 API Docs

Visit `/swagger/` to view API documentation.

---


---

## 📌 Notes

- Only the plant owner can access the system.  
- Not for public sales or buyers.  
- Deployed on PythonAnywhere with SQLite.

---
