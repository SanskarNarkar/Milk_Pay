🥛 Milk Pay – Milk Collection Management System

A Django-based web application developed to manage dairy milk collection records efficiently.
The system allows administrators to register farmers, record milk entries, calculate payments automatically based on fat percentage, and generate monthly summaries.

This project digitizes traditional dairy record management, improving accuracy, transparency, and efficiency. Similar dairy management applications are commonly built with Python, Django, and databases like SQLite or MySQL to track milk production and transactions.

🔗 Project Repository

GitHub Repository:

https://github.com/SanskarNarkar/Milk_Pay.git

📌 Features
🔐 Authentication System
Secure login and logout
Role-based access
Admin and Farmer dashboards

👨‍💼 Admin Features

Admin can:

Register new farmers
Edit farmer details
Delete farmers
Add milk collection entries
Edit milk entries
Update milk rates (Cow / Buffalo)
View monthly milk collection records
Filter records by farmer and month
👨‍🌾 Farmer Features

Farmers can:

Login securely
View personal milk records
View monthly milk totals
Check payment summary
⚙️ Automatic Payment Calculation

Milk payment is calculated automatically using:

Rate = Fat × Base Price
Total Amount = Quantity × Rate

Example:

Fat = 5
Cow Rate = 6

Rate = 5 × 6 = 30
Quantity = 10 Liters

Total Amount = 10 × 30 = 300
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
Django	Backend web framework
HTML	Frontend structure
CSS / Bootstrap	UI design
SQLite	Database
Django Authentication	User management
🗂️ Project Structure
Milk_Pay/
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

Stores milk collection records.

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

Stores milk pricing configuration.

Field	Description
price_cow_fat	Cow milk rate
price_buffalo_fat	Buffalo milk rate
updated_at	Last update timestamp
🚀 How to Run the Project

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/SanskarNarkar/Milk_Pay.git
cd Milk_Pay

2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing:
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
------------------------------------------
📊 System Workflow
Admin
Login
Register farmers
Set milk rates
Add milk entries
View monthly reports
Farmer
Login
View milk records
Check total payment


📷 Screenshots
<img width="1679" height="864" alt="image" src="https://github.com/user-attachments/assets/87994e27-f8ae-40bf-9bfd-7af9dd8ce26b" />
<img width="1042" height="859" alt="image" src="https://github.com/user-attachments/assets/33c5d838-b76b-4096-90c0-34098416fb28" />


screenshots/login.png
screenshots/admin_dashboard.png
screenshots/farmer_dashboard.png
🚀 Future Improvements

Possible enhancements:

Payment tracking system
Export reports to PDF / Excel
SMS notifications to farmers
Graph-based analytics dashboard
Mobile application integration


👨‍💻 Author
Developed by Sanskar Narkar


GitHub:
https://github.com/SanskarNarkar

Project Repository:
https://github.com/SanskarNarkar/Milk_Pay.git
