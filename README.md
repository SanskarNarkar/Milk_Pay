# 🥛 Milk Pay – Milk Collection Management System

A Django-based web application developed to manage dairy milk collection records efficiently.

The system allows administrators to:

- Register farmers
- Record milk entries
- Calculate payments automatically based on fat percentage
- Generate monthly milk reports

This project digitizes traditional dairy record management and improves **accuracy, transparency, and efficiency**.

---

## 🔗 Project Repository

https://github.com/SanskarNarkar/Milk_Pay

---

# 📌 Features

## 🔐 Authentication System
- Secure login and logout
- Role-based access control
- Admin and Farmer dashboards

---

## 👨‍💼 Admin Features

Admin can:

- Register new farmers
- Edit farmer details
- Delete farmers
- Add milk collection entries
- Edit milk entries
- Update milk rates (Cow / Buffalo)
- View monthly milk collection reports
- Filter records by month and farmer

---

## 👨‍🌾 Farmer Features

Farmers can:

- Login securely
- View personal milk records
- View monthly milk totals
- Check total earnings

---

# ⚙️ Automatic Payment Calculation

Milk payment is calculated automatically:

Rate = Fat × Base Price  
Total Amount = Quantity × Rate

Example:

Fat = 5  
Cow Rate = 6  

Rate = 5 × 6 = 30  

Quantity = 10 Liters  

Total Amount = 10 × 30 = 300

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Django | Backend framework |
| HTML | Frontend structure |
| CSS / Bootstrap | UI styling |
| SQLite | Database |

---

# 🚀 How to Run the Project

### 1 Clone Repository
git clone https://github.com/SanskarNarkar/Milk_Pay.git

cd Milk_Pay

### 2 Create Virtual Environment

python -m venv venv

Activate environment:
Windows

venv\Scripts\activate
Linux / Mac

source venv/bin/activate

### 3 Install Dependencies
pip install -r requirements.txt

### 4 Apply Database Migrations


python manage.py makemigrations
python manage.py migrate

### 5 Create Admin User

python manage.py createsuperuser

### 6 Run Server

python manage.py runserver

Open browser:
http://127.0.0.1:8000


---

# 📊 System Workflow

### Admin

1 Login  
2 Register farmers  
3 Set milk rates  
4 Add milk entries  
5 View monthly reports  

### Farmer

1 Login  
2 View milk records  
3 Check total payment  

---

# 🚀 Future Improvements

- Payment tracking system
- Export reports to PDF / Excel
- SMS notifications to farmers
- Graph-based analytics dashboard
- Mobile application integration

---

# 👨‍💻 Author

Developed by **Sanskar Narkar**

GitHub:  
https://github.com/SanskarNarkar
