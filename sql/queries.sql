-- 1. Total funds
SELECT COUNT(*) AS total_funds
FROM dim_fund;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Highest NAV fund
SELECT fund_id, MAX(nav) AS highest_nav
FROM fact_nav;

-- 4. Lowest NAV fund
SELECT fund_id, MIN(nav) AS lowest_nav
FROM fact_nav;

-- 5. Average transaction amount
SELECT AVG(amount) AS avg_transaction
FROM fact_transactions;

-- 6. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Average 1Y return
SELECT AVG(return_1y)
FROM fact_performance;

-- 8. Top fund by 1Y return
SELECT fund_id, return_1y
FROM fact_performance
ORDER BY return_1y DESC
LIMIT 1;

-- 9. Average expense ratio
SELECT AVG(expense_ratio)
FROM fact_performance;

-- 10. Risk grade distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;