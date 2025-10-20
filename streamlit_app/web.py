import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("AI-Based Inventory Management Dashboard")

# ------------------- Products -------------------
st.header("Products")

# Load Products
if st.button("Load Products"):
    try:
        res = requests.get(f"{API_URL}/products")
        res.raise_for_status()
        products = res.json()
        st.table(products)
    except Exception as e:
        st.error(f"Failed to load products: {e}")

# Add Product
st.subheader("Add New Product")
with st.form("add_product_form"):
    name = st.text_input("Product Name")
    category = st.text_input("Category")
    current_stock = st.number_input("Current Stock", min_value=0, step=1)
    reorder_level = st.number_input("Reorder Level", min_value=0, step=1)
    submitted = st.form_submit_button("Add Product")
    if submitted:
        payload = {
            "name": name,
            "category": category,
            "current_stock": current_stock,
            "reorder_level": reorder_level
        }
        try:
            res = requests.post(f"{API_URL}/products/", json=payload)
            res.raise_for_status()
            st.success("Product added successfully!")
        except Exception as e:
            st.error(f"Failed to add product: {e}")

# ------------------- Sales -------------------
st.header("Record Sale")
with st.form("add_sale_form"):
    product_id = st.number_input("Product ID", min_value=1, step=1)
    quantity = st.number_input("Quantity Sold", min_value=1, step=1)
    submitted = st.form_submit_button("Record Sale")
    if submitted:
        payload = {"product_id": product_id, "quantity": quantity}
        try:
            res = requests.post(f"{API_URL}/sales/", json=payload)
            res.raise_for_status()
            st.success("Sale recorded successfully!")
        except Exception as e:
            st.error(f"Failed to record sale: {e}")

# ------------------- Forecast -------------------
st.header("Forecast Demand")
product_id_forecast = st.number_input("Enter Product ID for Forecast", min_value=1, step=1)
if st.button("Predict Demand"):
    try:
        res = requests.get(f"{API_URL}/forecast/{product_id_forecast}")
        res.raise_for_status()
        data = res.json()
        st.write(f"Predicted demand: {data.get('predicted_demand')}")
        st.write(f"Current stock: {data.get('current_stock')}")
        st.write(f"Stock gap: {data.get('stock_gap')}")
        if data.get("stock_gap", 0) > 0:
            st.warning("Stock below predicted demand!")
    except Exception as e:
        st.error(f"Forecast failed: {e}")
