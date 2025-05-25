```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP,
    total_amount DECIMAL(10, 2),
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE invoices (
    id INT PRIMARY KEY,
    customer_id INT,
    invoice_date TIMESTAMP,
    total_amount DECIMAL(10, 2),
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    hire_date TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE job_applications (
    id INT PRIMARY KEY,
    candidate_id INT,
    job_id INT,
    application_date TIMESTAMP,
    status VARCHAR(50),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

CREATE TABLE candidates (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE interviews (
    id INT PRIMARY KEY,
    candidate_id INT,
    interviewer_id INT,
    interview_date TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id),
    FOREIGN KEY (interviewer_id) REFERENCES employees(id)

);

CREATE TABLE payments (
    id INT PRIMARY KEY,
    order_id INT,
    payment_date TIMESTAMP,
    amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE shipments (
    id INT PRIMARY KEY,
    order_id INT,
    shipping_date TIMESTAMP,
    tracking_number VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE suppliers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    contact_person VARCHAR(100),
    contact_number VARCHAR(20)
);

CREATE TABLE purchases (
    id INT PRIMARY KEY,
    supplier_id INT,
    purchase_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE refunds (
    id INT PRIMARY KEY,
    order_id INT,
    refund_date TIMESTAMP,
    amount DECIMAL(10, 2),
    reason TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE returns (
    id INT PRIMARY KEY,
    order_id INT,
    return_date TIMESTAMP,
    reason TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE reviews (
    id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    review_date TIMESTAMP,
    rating INT,
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE support_tickets (
    id INT PRIMARY KEY,
    customer_id INT,
    subject VARCHAR(100),
    created_at TIMESTAMP,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE knowledge_articles (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    content TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE assets (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    purchase_date TIMESTAMP
);

CREATE TABLE projects (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    start_date TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE tasks (
    id INT PRIMARY KEY,
    project_id INT,
    name VARCHAR(100),
    description TEXT,
    due_date TIMESTAMP,
    status VARCHAR(50),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE milestones (
    id INT PRIMARY KEY,
    project_id INT,
    name VARCHAR(100),
    due_date TIMESTAMP,
    status VARCHAR(50),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE budgets (
    id INT PRIMARY KEY,
    project_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE expenses (
    id INT PRIMARY KEY,
    project_id INT,
    description TEXT,
    amount DECIMAL(10, 2),
    expense_date TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);


CREATE TABLE accounts (
    id INT PRIMARY KEY,
    account_number VARCHAR(50),
    account_type VARCHAR(50),
    balance DECIMAL(10,2)
);

CREATE TABLE transactions (
    id INT PRIMARY KEY,
    account_id INT,
    transaction_date TIMESTAMP,
    amount DECIMAL(10,2),
    transaction_type VARCHAR(50),
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);
```