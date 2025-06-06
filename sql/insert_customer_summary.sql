INSERT INTO customer_summary (
    CUSTOMER_ID, NAME, GENDER, JOIN_DATE, 
    CALL_MINUTES, DATA_USAGE_GB, 
    COMPLAINT_TYPE, COMPLAINT_DATE, MONTH
) VALUES (20, 'Ali Ahmad', 'Male', TO_DATE('2022-01-15', 'YYYY-MM-DD'), 320, 3.5, NULL, NULL, '2025-05');

INSERT INTO customer_summary VALUES (22, 'Sara Mansour', 'Female', TO_DATE('2021-06-01', 'YYYY-MM-DD'), 120, 1.2, 'Billing Issue', TO_DATE('2025-05-15', 'YYYY-MM-DD'), '2025-05');

INSERT INTO customer_summary VALUES (30, 'Khaled Tarek', 'Male', TO_DATE('2023-03-10', 'YYYY-MM-DD'), 200, 2.1, 'Network Outage', TO_DATE('2025-05-10', 'YYYY-MM-DD'), '2025-05');

INSERT INTO customer_summary VALUES (40, 'Nada Fawaz', 'Female', TO_DATE('2023-07-25', 'YYYY-MM-DD'), 180, 3.0, NULL, NULL, '2025-05');

INSERT INTO customer_summary VALUES (50, 'Hassan Saleh', 'Male', TO_DATE('2020-12-05', 'YYYY-MM-DD'), 250, 4.2, 'Late Installation', NULL, '2025-05');

INSERT INTO customer_summary VALUES (60, 'Lina Kassem', 'Female', TO_DATE('2021-09-09', 'YYYY-MM-DD'), 0, 1.0, 'Service Interruption', TO_DATE('2025-05-14', 'YYYY-MM-DD'), '2025-05');

INSERT INTO customer_summary VALUES (70, 'Omar Deeb', 'Male', TO_DATE('2019-05-30', 'YYYY-MM-DD'), 100, 0.8, 'Payment Error', TO_DATE('2025-05-15', 'YYYY-MM-DD'), '2025-05');

INSERT INTO customer_summary VALUES (80, 'Maya Alwan', 'Female', TO_DATE('2022-10-18', 'YYYY-MM-DD'), 310, 5.0, NULL, NULL, '2025-05');

INSERT INTO customer_summary VALUES (90, 'Rami Yousef', 'Male', TO_DATE('2023-01-11', 'YYYY-MM-DD'), 220, 2.5, 'Wrong Bill', TO_DATE('2025-05-16', 'YYYY-MM-DD'), '2025-05');

INSERT INTO customer_summary VALUES (100, 'Dina Baroud', 'Female', TO_DATE('2021-04-04', 'YYYY-MM-DD'), 190, 3.3, 'Router Issue', TO_DATE('2025-05-09', 'YYYY-MM-DD'), '2025-05');

commit;