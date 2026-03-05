SELECT
    amount_category,
    total_transactions,
    fraud_transactions,
    avg_amount,
    round(100* fraud_transactions/total_transactions,4) as fraud_percentage
FROM 
(
    SELECT
        CASE 
            WHEN amount <50 then 'low'
            WHEN amount between 50 and 200 then 'medium'
            ELSE 'high'
        END as amount_category,
        count(*) as total_transactions,
        sum(class) as fraud_transactions,
        round(avg(amount),2) as avg_amount
    FROM credit_transactions
    GROUP BY amount_category
) t;
