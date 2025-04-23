# 🚀 Streamlit + PostgreSQL in Docker
This is a multi-container application using Docker Compose.
It consists of:

A PostgreSQL database container preloaded with sample data

A Streamlit app container that queries and displays that data

# 📁 Project Structure
csharp
Copy
Edit
streamlit-postgresql-docker/
├── app/
│   └── app.py
├── db/
│   └── init.sql
├── requirements.txt
├── docker-compose.yml
└── README.md

# 🐳 How to Run This Project

1. ✅ Prerequisites
Docker & Docker Compose installed

2. 🔧 Build and Run the Containers
bash
Copy
Edit
docker-compose up --build
3. 🌐 Access the Streamlit App
Open your browser and go to:

http
Copy
Edit
http://localhost:8501
🧾 What Each File Does
app/app.py
Your main Streamlit app. It connects to PostgreSQL and fetches data using psycopg2.

db/init.sql
SQL script that auto-runs on PostgreSQL startup. It creates tables and inserts data.

docker-compose.yml
Defines the two services (db, streamlit) and connects them via Docker bridge networking.

requirements.txt
Specifies the Python dependencies like streamlit and psycopg2.

# 🧠 Key Concepts Demonstrated
Docker multi-container app setup

Bridged networking between containers

Python-PostgreSQL integration

Data visualization using Streamlit


