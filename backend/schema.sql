-- tables for the expense tracker (mysql on clever cloud)
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- dummy row for the tests
INSERT INTO expenses (expense_date, amount, category, notes)
SELECT '2024-08-15', 10, 'Shopping', 'Bought potatoes'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM expenses WHERE expense_date = '2024-08-15');
