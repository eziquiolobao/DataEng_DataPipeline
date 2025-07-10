import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

# Get database credentials from environment variables
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_NAME = os.getenv('POSTGRES_DB', 'eziquio')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
CSV_PATH = os.getenv('REDFIN_CSV_PATH', 'data/redfin_harvard_ma.csv')

TABLE_NAME = 'stg_redfin_sales'


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names and convert data types."""
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # Basic datatype cleaning
    if 'sold_date' in df.columns:
        df['sold_date'] = pd.to_datetime(df['sold_date'], errors='coerce')
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    if 'beds' in df.columns:
        df['beds'] = pd.to_numeric(df['beds'], errors='coerce')
    if 'baths' in df.columns:
        df['baths'] = pd.to_numeric(df['baths'], errors='coerce')
    if 'square_feet' in df.columns:
        df['square_feet'] = pd.to_numeric(df['square_feet'], errors='coerce')
    return df


def load_csv():
    df = pd.read_csv(CSV_PATH)
    df = clean_columns(df)

    # Establish psycopg2 connection (optional, for direct use)
    psycopg2_conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    # You can use psycopg2_conn.cursor() here if needed

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    with engine.connect() as conn:
        df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    print(f"Loaded {len(df)} rows into {TABLE_NAME}")


if __name__ == '__main__':
    load_csv()
