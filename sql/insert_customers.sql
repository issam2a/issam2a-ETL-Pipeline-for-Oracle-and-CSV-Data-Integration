-- Table 1: Customers
CREATE TABLE customers (
    customer_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    gender VARCHAR2(10),
    join_date DATE
);

-- Table 2: Final Cleaned Summary Table
CREATE TABLE customer_summary (
    customer_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    gender VARCHAR2(10),
    join_date DATE,
    call_minutes NUMBER,
    data_usage_gb NUMBER,
    complaint_type VARCHAR2(100),
    complaint_date DATE,
    month VARCHAR2(7)
);
