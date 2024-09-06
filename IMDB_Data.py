import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(dotenv_path = 'C:/Users/laton/OneDrive/Desktop/Personal Projects/pythonProject/.env.txt')

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST') 
database = os.getenv('MYSQL_DATABASE')

data = pd.read_csv("C:/Users/laton/OneDrive/Desktop/DATA/imdb_top_1000.csv")

df = pd.DataFrame(data)
df_updated = df[['Series_Title', 'Released_Year', 'Certificate', 'Genre', 'Runtime', 'IMDB_Rating', 'Meta_score', 'Director']]
print(df_updated)

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
table_name = 'movies'
df_updated.to_sql(table_name, con=engine, if_exists='replace', index=False)

