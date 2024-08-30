from fpdf import FPDF


class DetailedPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "MySQL Mastery in One Month: A Comprehensive Guide", 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, "L", 1)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_code_block(self, code):
        self.set_font("Courier", "I", 10)
        self.set_fill_color(230, 230, 230)
        self.multi_cell(0, 10, code, 0, 1, "L", 1)
        self.ln()


# Create PDF instance
detailed_pdf = DetailedPDF()

# Add a page
detailed_pdf.add_page()

# Set title
detailed_pdf.set_title("MySQL Mastery in One Month: A Comprehensive Guide")

# Introduction
detailed_pdf.chapter_title("Introduction")
intro_text = """\
This guide is designed to help you master MySQL in one month. It includes a structured learning plan, covering fundamental to advanced topics, and practical exercises. Each week focuses on different aspects of MySQL, providing you with a comprehensive understanding and hands-on experience.
"""
detailed_pdf.chapter_body(intro_text)

# Week 1
detailed_pdf.chapter_title("Week 1: Fundamentals")

# Day 1: Installation and Basic Commands
detailed_pdf.chapter_title("Day 1: Installation and Basic Commands")
day1_text = """\
Installation:
- Download and install MySQL from the official website.
- Install MySQL Workbench for a GUI interface.

Basic Commands:
- Start MySQL server: mysql.server start
- Stop MySQL server: mysql.server stop
- Connect to MySQL: mysql -u root -p
"""
detailed_pdf.chapter_body(day1_text)
detailed_pdf.add_code_block(
    """-- Show databases
SHOW DATABASES;

-- Create a new database
CREATE DATABASE testdb;

-- Use a database
USE testdb;"""
)

# Day 2: Database Design
detailed_pdf.chapter_title("Day 2: Database Design")
day2_text = """\
Database Design Basics:
- Understand tables, columns, and data types.
- Primary keys uniquely identify rows.
- Foreign keys link tables together.
"""
detailed_pdf.chapter_body(day2_text)
detailed_pdf.add_code_block(
    """-- Create a users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

-- Create an orders table with a foreign key
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""
)

# Day 3: CRUD Operations
detailed_pdf.chapter_title("Day 3: CRUD Operations")
day3_text = """\
Create, Read, Update, Delete:
- Insert data into tables.
- Select data from tables.
- Update existing data.
- Delete data.
"""
detailed_pdf.chapter_body(day3_text)
detailed_pdf.add_code_block(
    """-- Insert data
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');

-- Select data
SELECT * FROM users;

-- Update data
UPDATE users SET name = 'Jane Doe' WHERE id = 1;

-- Delete data
DELETE FROM users WHERE id = 1;"""
)

# Day 4: Constraints and Data Types
detailed_pdf.chapter_title("Day 4: Constraints and Data Types")
day4_text = """\
Constraints:
- NOT NULL, UNIQUE, CHECK, DEFAULT constraints.
- Ensuring data integrity.
"""
detailed_pdf.chapter_body(day4_text)
detailed_pdf.add_code_block(
    """-- Create a table with constraints
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) CHECK (price > 0),
    stock INT DEFAULT 0
);

Data Types:
- Understand various data types: INT, VARCHAR, DATE, etc.
"""
)

# Day 5: Relationships and Foreign Keys
detailed_pdf.chapter_title("Day 5: Relationships and Foreign Keys")
day5_text = """\
Relationships:
- One-to-One, One-to-Many, Many-to-Many relationships.
- Use foreign keys to enforce relationships.
"""
detailed_pdf.chapter_body(day5_text)
detailed_pdf.add_code_block(
    """-- One-to-Many relationship example
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
"""
)

# Day 6: Basic Queries
detailed_pdf.chapter_title("Day 6: Basic Queries")
day6_text = """\
Basic Queries:
- SELECT, WHERE, ORDER BY, LIMIT clauses.
- Filtering and sorting data.
"""
detailed_pdf.chapter_body(day6_text)
detailed_pdf.add_code_block(
    """-- Select with filtering and sorting
SELECT * FROM products WHERE price > 50 ORDER BY price DESC LIMIT 10;
"""
)

# Day 7: Review and Practice
detailed_pdf.chapter_title("Day 7: Review and Practice")
day7_text = """\
Review:
- Recap the concepts learned throughout the week.
- Practice by creating small sample databases and performing CRUD operations.
"""
detailed_pdf.chapter_body(day7_text)

# Week 2: Intermediate Concepts
detailed_pdf.chapter_title("Week 2: Intermediate Concepts")

# Day 8: Advanced Queries
detailed_pdf.chapter_title("Day 8: Advanced Queries")
day8_text = """\
Advanced Queries:
- Practice using complex queries involving JOINs, subqueries, and aggregate functions (COUNT, SUM, AVG, etc.).
"""
detailed_pdf.chapter_body(day8_text)
detailed_pdf.add_code_block(
    """-- Join example
SELECT u.name, o.order_date 
FROM users u 
JOIN orders o ON u.id = o.user_id;

-- Aggregate function example
SELECT COUNT(*), AVG(price) 
FROM products;
"""
)

# Day 9: Indexing
detailed_pdf.chapter_title("Day 9: Indexing")
day9_text = """\
Indexing:
- Learn about indexes, how to create them, and their impact on query performance.
"""
detailed_pdf.chapter_body(day9_text)
detailed_pdf.add_code_block(
    """-- Create index
CREATE INDEX idx_user_name ON users(name);

-- Create composite index
CREATE INDEX idx_product_name_price ON products(name, price);
"""
)

# Day 10: Transactions
detailed_pdf.chapter_title("Day 10: Transactions")
day10_text = """\
Transactions:
- Understand transactions, commit, rollback, and isolation levels.
"""
detailed_pdf.chapter_body(day10_text)
detailed_pdf.add_code_block(
    """-- Transaction example
START TRANSACTION;
UPDATE users SET balance = balance - 100 WHERE id = 1;
UPDATE users SET balance = balance + 100 WHERE id = 2;
COMMIT;
"""
)

# Day 11: Stored Procedures and Functions
detailed_pdf.chapter_title("Day 11: Stored Procedures and Functions")
day11_text = """\
Stored Procedures and Functions:
- Learn how to create and use stored procedures and functions.
"""
detailed_pdf.chapter_body(day11_text)
detailed_pdf.add_code_block(
    """-- Stored procedure example
DELIMITER //
CREATE PROCEDURE GetUser(IN userId INT)
BEGIN
    SELECT * FROM users WHERE id = userId;
END //
DELIMITER ;

-- Call stored procedure
CALL GetUser(1);
"""
)

# Day 12: User-Defined Variables and Views
detailed_pdf.chapter_title("Day 12: User-Defined Variables and Views")
day12_text = """\
User-Defined Variables and Views:
- Using variables for temporary storage and reusable queries with views.
"""
detailed_pdf.chapter_body(day12_text)
detailed_pdf.add_code_block(
    """-- User-defined variable example
SET @total_sales = (SELECT SUM(price) FROM sales);
SELECT @total_sales;

-- Create view
CREATE VIEW active_users AS
SELECT * FROM users WHERE status = 'active';
"""
)

# Day 13: Review and Practice
detailed_pdf.chapter_title("Day 13: Review and Practice")
day13_text = """\
Review:
- Recap the concepts learned throughout the week.
- Practice by writing advanced queries and using indexes, transactions, and stored procedures.
"""
detailed_pdf.chapter_body(day13_text)

# Save the first part of the PDF
pdf_path_part1 = "/mnt/data/MySQL_Mastery_Part1.pdf"
detailed_pdf.output(pdf_path_part1)

pdf_path_part1
