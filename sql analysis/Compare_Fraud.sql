
select 
    class, 
    round(avg(amount),2) as avg_transaction_amt,
    round(max(amount),2) as max_transaction_amt
from credit_transactions
group by class; 