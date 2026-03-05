select class, count(*) as total_transactions from credit_transactions group by class;
select round(100 * sum(class)/count(*),4) as percentage_fraudulent from credit_transactions;