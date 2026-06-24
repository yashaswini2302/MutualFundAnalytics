# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| fund_id | INTEGER | Primary key |
| amfi_code | INTEGER | AMFI scheme code |
| fund_name | TEXT | Mutual fund name |
| fund_house | TEXT | Fund house |
| scheme_type | TEXT | Scheme type |
| scheme_category | TEXT | Fund category |

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| nav_id | INTEGER | Primary key |
| fund_id | INTEGER | Fund reference |
| date_id | INTEGER | Date reference |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| transaction_id | INTEGER | Transaction ID |
| investor_id | INTEGER | Investor ID |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount | REAL | Transaction amount |
| transaction_date | DATE | Transaction date |
| kyc_status | TEXT | KYC status |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| performance_id | INTEGER | Primary key |
| fund_id | INTEGER | Fund reference |
| return_1y | REAL | 1 year return |
| return_3y | REAL | 3 year return |
| return_5y | REAL | 5 year return |
| expense_ratio | REAL | Expense ratio |
| risk_grade | TEXT | Risk category |