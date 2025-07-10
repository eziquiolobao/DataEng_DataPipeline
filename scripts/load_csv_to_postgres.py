import os
import pandas as pd
from sqlalchemy import create_engine

TABLE_NAME = 'stg_redfin_sales'


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names and convert data types."""
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
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


def load_csv(
    db_host: str | None = None,
    db_port: str | None = None,
    db_name: str | None = None,
    db_user: str | None = None,
    db_password: str | None = None,
    csv_path: str | None = None,
) -> None:
    """Load a CSV file into Postgres."""
    db_host = db_host or os.getenv("POSTGRES_HOST")
    db_port = db_port or os.getenv("POSTGRES_PORT")
    db_name = db_name or os.getenv("POSTGRES_DB")
    db_user = db_user or os.getenv("POSTGRES_USER")
    db_password = db_password or os.getenv("POSTGRES_PASSWORD")
    csv_path = csv_path or os.getenv("REDFIN_CSV_PATH")

    df = pd.read_csv(csv_path)
    df = clean_columns(df)

    engine = create_engine(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    with engine.connect() as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into {TABLE_NAME}")


if __name__ == "__main__":
    load_csv()
