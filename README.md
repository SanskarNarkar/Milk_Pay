🥛 Milk Collection Management System

A Django-based web application designed to manage milk collection records for dairy farms.
The system allows administrators to manage farmers, record milk entries, calculate payments automatically based on fat percentage, and generate monthly summaries.

This project digitizes traditional dairy record management and improves accuracy, transparency, and efficiency.


📌 Features
🔐 Authentication System
Secure login and logout
Role-based access control
Admin and Farmer dashboards
-------------------------------------------------
👨‍💼 Admin Features

Admin can:
Register new farmers
Edit farmer details
Delete farmers
Add milk collection entries
Edit milk entries
Update milk rates (Cow / Buffalo)
View monthly milk collection reports
Filter records by month and farmer

---------------------------------------------------
👨‍🌾 Farmer Features

Farmers can:
Login securely
View personal milk records
View monthly milk totals
Check total earnings

⚙️ Automatic Payment Calculation
Milk payment is calculated automatically:

Rate = Fat × Base Price
Total Amount = Quantity × Rate

Example:

Fat = 5
Cow Rate = 6

Rate = 5 × 6 = 30
Quantity = 10 Liters

Total Amount = 10 × 30 = 300

🛠️ Technologies Used
-----------------------------------------------------
Technology	Purpose
Python	Programming language
Django	Backend framework
HTML	Frontend structure
CSS / Bootstrap	UI styling
SQLite	Database
Django Authentication	Login system

----------------------------------------------------
🗂️ Project Structure
milkproject/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── admin_dashboard.html
│   │       ├── farmer_dashboard.html
│   │       ├── login.html
│   │       ├── register_farmer.html
│   │       ├── edit_entry.html
│   │       └── edit_farmer.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
│
├── milkproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt

----------------------------------------------------------
🗃️ Database Models
User
Custom user model extending Django authentication.

Fields:
username
password
phone
address
is_farmer
is_admin
MilkEntry
-----------------------------------------------
Stores milk collection records.
Fields:
Field	Description
farmer	Linked farmer
date	Collection date
shift	Morning / Evening
milk_type	Cow / Buffalo
fat	Fat percentage
quantity	Milk quantity
rate_applied	Calculated rate
total_amount	Final payment
RateConfig
-------------------------------------------------
Stores milk pricing configuration.
Fields:
Field	Description
price_cow_fat	Cow milk rate
price_buffalo_fat	Buffalo milk rate
updated_at	Last updated time

-----------------------------------
🚀 How to Run the Project

Follow these steps to run the project locally.

1️⃣ Clone Repository
git clone https://github.com/yourusername/milk-collection-system.git
cd milk-collection-system

2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements file doesn't exist:
pip install django

4️⃣ Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Admin User
python manage.py createsuperuser

Enter:
username
email
password

6️⃣ Run Development Server
python manage.py runserver

Open browser:
http://127.0.0.1:8000

---------------------------------------------
🧑‍💻 System Workflow
Admin
1️⃣ Login
2️⃣ Register farmers
3️⃣ Set milk rates
4️⃣ Add milk entries
5️⃣ View monthly reports

Farmer

1️⃣ Login
2️⃣ View milk records
3️⃣ Check monthly totals
-------------------------------------------
📊 Future Improvements
Possible future upgrades:

Payment tracking system
Export reports to PDF / Excel
SMS notification for farmers
Graph-based analytics dashboard
Mobile app integration


📷 Screenshots

<img width="1042" height="859" alt="image" src="https://github.com/user-attachments/assets/2088a7f4-9b80-4486-9230-20a0d881e01e" />

<img width="1679" height="864" alt="image" src="https://github.com/user-attachments/assets/26f999a0-6e30-46f0-9e1d-ab533eda9dfe" />


📄 License

This project is created for educational purposes.

👨‍💻 Author

Developed by Sanskar

GitHub
https://github.com/
