🧠 AI-Based Inventory Management

A full-stack application for managing inventory, sales, and demand forecasting using FastAPI, MySQL, and Streamlit. It combines robust backend APIs, intelligent forecasting models, and an interactive web dashboard.

✨ Features

📦 Product Management – Add, list, and track products in inventory.

💰 Sales Management – Record and analyze product sales.

📈 Demand Forecasting – Predict future demand using machine learning models.

📊 Web Dashboard – Interactive Streamlit frontend for managing inventory and visualizing forecasts.

⚙️ Configuration Management – Uses .env for secure environment variables and credentials.

🧱 Tech Stack
Component	Technology
Backend	FastAPI
Database	MySQL (via SQLAlchemy ORM)
Frontend	Streamlit
Machine Learning	Forecasting models in Python (app/ml/)
Environment Management	.env for sensitive credentials
📁 Folder Structure

AI_Based_InventoryManagement/
│
├── app/ # Backend logic (FastAPI)
│ ├── config.py # Database configuration
│ ├── crud/ # CRUD operations
│ ├── models/ # Database models
│ ├── routes/ # API routes
│ └── schemas/ # Pydantic schemas
│
├── streamlit_app/ # Streamlit frontend
│ └── app.py
│
├── main.py # FastAPI entry point
├── requirements.txt # Project dependencies
├── test_db.py # Optional: test DB connection
└── .env # Environment variables

⚙️ Installation
1. Clone the Repository

git clone https://github.com/sangam9170/AI_Based_InventoryManagement.git

cd AI_Based_InventoryManagement

2. Create Virtual Environment & Install Dependencies

python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
pip install -r requirements.txt

🚀 Run the Application
1. Start FastAPI Backend

python -m uvicorn main:app --reload
API Documentation → http://127.0.0.1:8000/docs

2. Start Streamlit Frontend

streamlit run streamlit_app/app.py
Streamlit Dashboard will open automatically in your default browser.

🧩 Test Database Connection

python test_db.py
Expected Output:
Database connected successfully!

🤝 Contributing

Fork the repository

Create a feature branch → git checkout -b feature_name

Commit your changes → git commit -m "Description of your change"

Push to your branch → git push origin feature_name

Open a Pull Request

🧾 Git Push Commands (Quick Reference)

git init
git add .
git commit -m "Initial commit - AI-Based Inventory Management"
git remote add origin https://github.com/sangam9170/AI_Based_InventoryManagement.git

git branch -M main
git push -u origin main

📚 Future Enhancements

🤖 AI-based dynamic restocking alerts

📦 Barcode integration for real-time tracking

📅 Automated supplier order generation

🧾 Exportable reports (PDF, Excel)
