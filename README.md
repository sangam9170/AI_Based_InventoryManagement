🧠 AI-Based Inventory Management

A full-stack application for managing inventory, sales, and demand forecasting using FastAPI, MySQL, and Streamlit.
It combines robust backend APIs, intelligent forecasting models, and an interactive web dashboard.

⚡ Features

📦 Product Management – Add, list, and track products in inventory

💰 Sales Management – Record and analyze sales transactions

📈 Demand Forecasting – Predict future demand using machine learning models

📊 Web Dashboard – Interactive Streamlit UI for data visualization

⚙️ Secure Configurations – Environment variables managed via .env file

🧱 Tech Stack
Component	Technology
Backend	FastAPI
Database	MySQL (SQLAlchemy ORM)
Frontend	Streamlit
Machine Learning	Python (Forecasting models in app/ml/)
Environment Management	.env file for credentials
📂 Folder Structure
AI_Based_InventoryManagement/
│
├── app/                     # Backend logic (FastAPI)
│   ├── config.py            # Database configuration
│   ├── crud/                # CRUD operations
│   ├── models/              # Database models
│   ├── routes/              # API routes
│   └── schemas/             # Pydantic schemas
│
├── streamlit_app/           # Streamlit frontend
│   └── app.py
│
├── main.py                  # FastAPI entry point
├── requirements.txt         # Project dependencies
├── test_db.py               # Optional: Test database connection
└── .env                     # Environment variables

⚙️ Installation Steps
🧩 1️⃣ Clone the Repository
git clone https://github.com/sangam9170/AI_Based_InventoryManagement.git
cd AI_Based_InventoryManagement

🧩 2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt

🚀 Run the Application
▶️ Start FastAPI Backend
python -m uvicorn main:app --reload


📘 API Documentation: http://127.0.0.1:8000/docs

💻 Start Streamlit Frontend
streamlit run streamlit_app/app.py


🌐 The Streamlit dashboard will open automatically in your browser.

🧩 Test Database Connection
python test_db.py


✅ Expected Output:

Database connected successfully!

🤝 Contributing

We welcome community contributions! Follow these steps:

Fork the repository

Create a feature branch

git checkout -b feature_name


Commit your changes

git commit -m "Added new feature"


Push to your branch

git push origin feature_name


Open a Pull Request

🧾 Git Commands (Quick Reference)
git init
git add .
git commit -m "Initial commit - AI-Based Inventory Management"
git remote add origin https://github.com/sangam9170/AI_Based_InventoryManagement.git
git branch -M main
git push -u origin main

🚧 Future Enhancements

🤖 AI-based dynamic restocking alerts

📦 Barcode integration for real-time tracking

📅 Automated supplier order generation

🧾 Exportable reports (PDF, Excel)

👨‍💻 Developed By

Sangam Singh

🎯 Empowering smart inventory through AI-driven insights.
