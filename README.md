# 📊 ETL Pipeline for Oracle and CSV Data Integration

## 🧠 Overview

This project demonstrates an **ETL (Extract, Transform, Load)** pipeline that integrates customer data from an **Oracle database** and **CSV files** into a unified format suitable for business analysis — especially **customer churn analysis**. The project ensures consistent, clean data across sources before loading it into a target Oracle table.

---

## 🚀 Project Features

- Extract data from an Oracle database and CSV file
- Clean and standardize data using Pandas
- Handle missing values, type mismatches, and indexing issues
- Load clean data into a target Oracle database table
- Modular Python design with reusable components
- Error handling and transformation logic included

---

## 🔧 Technologies Used

- **Python 3.10+**
- **Pandas** for data manipulation
- **Oracledb** for Oracle DB integration
- **Oracle 19c** (local or remote)
- **CSV** for flat file ingestion
- **Virtual Environment** for isolation

---

## 📁 Project Structure

ETL Pipeline for Oracle and CSV Data Integration/
├── main.py # Pipeline entry point
├── etl/
│ ├── extract.py # Functions to extract data
│ ├── transform.py # Cleaning and formatting logic
│ └── load.py # Load functions for Oracle
├── data/
│ └── customer_data.csv # Sample CSV data
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🛠️ ETL Pipeline Steps

### ✅ 1. Extract
- Connect to Oracle database and read data from table
- Load customer data from CSV using `pandas.read_csv()`

### 🔄 2. Transform
- Clean column names and ensure consistency
- Convert numeric fields (`monthlycharges`, `totalcharges`) to `float`
- Replace `NaN` with `None` to match Oracle’s `NULL`
- Drop rows with missing `customerID`

### 📤 3. Load
- Use `Oracledb` and `executemany()` to insert cleaned data into Oracle
- Ensure data type compatibility with Oracle column definitions

---

## 💡 Key Learnings

- Integrating mixed-source data into a unified schema
- Handling real-world data issues (missing values, type mismatches)
- Efficient bulk data loading into Oracle
- Building reusable and modular ETL code

---

## ▶️ Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/issam2a/issam2a-ETL-Pipeline-for-Oracle-and-CSV-Data-Integration.git
cd ETL Pipeline for Oracle and CSV Data Integration

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Run the Pipeline
Make sure Oracle is running and properly configured.


python main.py

📌 Oracle Table Schema

CREATE TABLE report (
  customerID         VARCHAR2(50) PRIMARY KEY,
  gender             VARCHAR2(10),
  seniorcitizen      NUMBER(1),
  partner            VARCHAR2(5),
  dependents         VARCHAR2(5),
  tenure             NUMBER,
  phoneservice       VARCHAR2(5),
  multiplelines      VARCHAR2(20),
  internetservice    VARCHAR2(20),
  onlinesecurity     VARCHAR2(20),
  onlinebackup       VARCHAR2(20),
  deviceprotection   VARCHAR2(20),
  techsupport        VARCHAR2(20),
  streamingtv        VARCHAR2(20),
  streamingmovies    VARCHAR2(20),
  contract           VARCHAR2(20),
  paperlessbilling   VARCHAR2(5),
  paymentmethod      VARCHAR2(50),
  monthlycharges     NUMBER(10,2),
  totalcharges       NUMBER(12,2),
  churn              VARCHAR2(5)
);
❗ Troubleshooting
Unsupported Python type float for VARCHAR?
Ensure numeric fields are inserted into numeric columns, and replace NaN with 0.



KeyError in Pandas?
Print df.columns to debug and correct mismatches.

📈 Future Improvements
Add logging and audit trail

Schedule with Airflow or cron jobs

Include unit tests for transform logic

Build a reporting dashboard from the final table


