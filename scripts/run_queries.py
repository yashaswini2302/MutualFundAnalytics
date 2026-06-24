import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

queries = [
    ("Total Funds",
     "SELECT COUNT(*) FROM dim_fund"),

    ("Average NAV",
     "SELECT AVG(nav) FROM fact_nav"),

    ("Highest NAV",
     "SELECT MAX(nav) FROM fact_nav"),

    ("Lowest NAV",
     "SELECT MIN(nav) FROM fact_nav"),

    ("Average Transaction Amount",
     "SELECT AVG(amount) FROM fact_transactions"),

    ("Transaction Count by Type",
     "SELECT transaction_type, COUNT(*) FROM fact_transactions GROUP BY transaction_type"),

    ("Average 1Y Return",
     "SELECT AVG(return_1y) FROM fact_performance"),

    ("Top 1Y Return",
     "SELECT MAX(return_1y) FROM fact_performance"),

    ("Average Expense Ratio",
     "SELECT AVG(expense_ratio) FROM fact_performance"),

    ("Risk Grade Distribution",
     "SELECT risk_grade, COUNT(*) FROM fact_performance GROUP BY risk_grade")
]

for title, query in queries:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

conn.close()