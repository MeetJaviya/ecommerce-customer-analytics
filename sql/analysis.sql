SHOW DATABASES;
CREATE DATABASE ecommerce;

USE ecommerce;

CREATE TABLE customers (

CustomerID INT,
Recency INT,
Frequency INT,
Monetary FLOAT,
Churn INT
);


LOAD DATA LOCAL INFILE 'C:/Users/Meet Javiya/Desktop/MYSQL/PROJECTS/ecommerce-customer-analytics/data/processed/rfm_data.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


SHOW TABLES from ecommerce;

SELECT * FROM customers LIMIT 10;


SELECT
AVG(Monetary)
FROM customers;



SELECT CustomerID, Monetary
FROM customers
ORDER BY Monetary DESC
LIMIT 10;

SELECT COUNT(*)
FROM customers
WHERE Churn = 1;

SELECT AVG(Frequency)
FROM customers;

SELECT AVG(Recency)
FROM customers;


select * from customers;

USE ecommerce;
CREATE TABLE sales ( InvoiceNo VARCHAR(20),StockCode VARCHAR(20),Description TEXT, Quantity INT,InvoiceDate DATETIME,UnitPrice FLOAT,CustomerID INT,Country VARCHAR(50),TotalPrice FLOAT);

LOAD DATA LOCAL INFILE 'C:/Users/Meet Javiya/Desktop/MYSQL/PROJECTS/ecommerce-customer-analytics/data/processed/cleaned_data.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


SELECT * from customers;
SELECT SUM(TotalPrice) FROM sales;










