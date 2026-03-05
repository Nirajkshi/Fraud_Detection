select 
    floor(time/86400) as day_number,
    count(*) as total_transactions,
    sum(class) as fraud_trns
FROM credit_transactions
GROUP BY day_number
ORDER BY day_number;