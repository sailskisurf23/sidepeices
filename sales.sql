BEGIN;

CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        birthyear INTEGER,
        city VARCHAR(50),
        state VARCHAR(2)
        );

CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        price NUMERIC(6, 2)
        );

CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY,
        custid INTEGER REFERENCES customers(id),
        prodid INTEGER REFERENCES products(id),
        quantity INTEGER,
        date DATE
        );

DELETE FROM customers;
DELETE FROM purchases;
DELETE FROM products;

INSERT INTO customers VALUES
        (1001, 'Polly', 1952, 'San Francisco', 'CA'),
        (1003, 'Chiron', 1980, 'Seattle', 'WA'),
        (1004, 'Petra', 1992, 'New York', 'NY'),
        (1005, 'Arvind', 1974, 'Phoenix', 'AZ');

INSERT INTO customers (id, name, city, state) VALUES
        (1006, 'Pei', 'Austin', 'TX'),
        (1002, 'Juan', 'Denver', 'CO');

INSERT INTO customers (id, name, birthyear, state) VALUES
        (1007, 'Pira', 1977, 'CA');

INSERT INTO products (id, name, price) VALUES
        (9001, 'Electric Razor', 59.99),
        (9002, 'Turkey Jerky',  3.59),
        (9003,  'Paper Towels',  4.15),
        (9004, 'Straightrazor', 15.12),
        (9005, 'Barcelona Chair', 1579.00);


INSERT INTO purchases (id, custid, prodid, quantity, date) VALUES
        (5501, 1001, 9003, 3, '2017-01-03'),
        (5502, 1003, 9002, 1, '2017-02-05'),
        (5503, 1001, 9001, 3, '2017-03-10'),
        (5004, 1006, 9002, 1, '2017-03-11');

COMMIT;
