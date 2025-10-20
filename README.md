

```markdown
# AI-Based Inventory Management

A full-stack application for managing inventory, sales, and demand forecasting using **FastAPI**, **MySQL**, and **Streamlit**.

---

## Features

- **Product Management**: Add, list, and track products in inventory.
- **Sales Management**: Record sales for products.
- **Demand Forecasting**: Predict future product demand using ML.
- **Web Dashboard**: Interactive Streamlit frontend for managing inventory and visualizing forecasts.

---

## Tech Stack

- **Backend**: FastAPI  
- **Database**: MySQL (via SQLAlchemy ORM)  
- **Frontend**: Streamlit  
- **ML**: Forecasting models in Python (inside `app/ml`)  
- **Environment Management**: `.env` for sensitive credentials  

---

## Folder Structure

```

AI_Based_InventoryManagement/
│
├── app/                  # Backend logic
│   ├── config.py         # DB config
│   ├── crud/             # CRUD operations
│   ├── models/           # Database models
│   ├── routes/           # API routes
│   └── schemas/          # Pydantic schemas
├── streamlit_app/        # Streamlit frontend
│   └── app.py
├── main.py               # FastAPI entry point
├── requirements.txt
├── test_db.py            # Optional DB connection test
└── .env                  # Environment variables

````

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/sangam9170/AI_Based_InventoryManagement.git
cd AI_Based_InventoryManagement
````

2. **Create virtual environment & install dependencies**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```

3. **Set up `.env` file**

```env
DB_USER=root
DB_PASSWORD=YourMySQLPassword
DB_HOST=localhost
DB_NAME=inventory_db
```

---

## Run Application

### 1. Start FastAPI Backend

```bash
python -m uvicorn main:app --reload
```

* API Docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Start Streamlit Frontend

```bash
streamlit run streamlit_app/app.py
```

* Streamlit Dashboard will open in your default browser.

---

## Testing Database Connection

```bash
python test_db.py
```

* Should print `Database connected successfully!` if connection is working.

---

## Contributing

* Fork the repo
* Create a feature branch (`git checkout -b feature_name`)
* Commit your changes (`git commit -m "Description"`)
* Push to branch (`git push origin feature_name`)
* Open a Pull Request

---

## License

This project is licensed under the MIT License.

````

---

### **Git Push Commands**
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - AI-Based Inventory Management"

# Add remote
git remote add origin https://github.com/sangam9170/AI_Based_InventoryManagement.git

# Push to main branch
git branch -M main
git push -u origin main
````


