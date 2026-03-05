from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:PASSWORD@localhost/fintech_analytics')
df = pd.read_csv('data/creditcard.csv')
df.to_sql('credit_transactions', con=engine, if_exists='replace', index=False)
print("Dataset loaded successfully into the database.")