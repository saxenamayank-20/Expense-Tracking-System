-- Run this once in the Neon SQL Editor.
CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Sample row used by testing/backend/test_database_helper.py
INSERT INTO expenses (expense_date, amount, category, notes)
SELECT '2024-08-15', 10, 'Shopping', 'Bought potatoes'
WHERE NOT EXISTS (SELECT 1 FROM expenses WHERE expense_date = '2024-08-15');
