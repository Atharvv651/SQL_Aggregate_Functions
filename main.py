CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('John', 'Doe', 'Sales', 60000, '2020-01-15'),
('Jane', 'Smith', 'Marketing', 75000, '2018-07-20'),
('Alice', 'Johnson', 'Sales', 65000, '2019-03-30');

INSERT INTO products (name, price, stock_quantity) VALUES
('Laptop', 1200.00, 30),
('Smartphone', 800.00, 50),
('Tablet', 400.00, 70);

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-02-15', 1500.00),
(2, '2023-03-10', 800.00),
(3, '2023-01-05', 400.00);

SELECT COUNT(*) AS total_employees FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(price) AS max_price FROM products;
SELECT MIN(price) AS min_price FROM products;

SELECT SUM(total_amount) AS total_revenue FROM orders;
SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;
SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department;

SELECT stock_quantity, COUNT(*) AS product_count FROM products GROUP BY stock_quantity;
