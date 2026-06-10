-- orders mart DDL (synthetic)
CREATE TABLE CUSTOMERS (id INT PRIMARY KEY, name TEXT, region TEXT);
CREATE TABLE ORDERS (
  order_id INT PRIMARY KEY,
  customer_id INT REFERENCES CUSTOMERS(id),
  order_date DATE, amount DECIMAL(12,2)
);
CREATE TABLE PAYMENTS (payment_id INT PRIMARY KEY, order_id INT, paid_at TIMESTAMP, amount DECIMAL(12,2));
CREATE TABLE SHIPMENTS (shipment_id INT PRIMARY KEY, order_ref INT, shipped_at TIMESTAMP, carrier TEXT);
CREATE TABLE INVOICES (invoice_no TEXT PRIMARY KEY, issued_at DATE, total DECIMAL(12,2));
CREATE TABLE stg_orders (raw_id INT, payload TEXT, loaded_at TIMESTAMP);
