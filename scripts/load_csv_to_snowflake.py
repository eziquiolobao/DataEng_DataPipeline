import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

TABLE_NAME = 'stg_house_sales'

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names and convert basic datatypes."""
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    if 'sold_date' in df.columns:
        df['sold_date'] = pd.to_datetime(df['sold_date'], errors='coerce')
    numeric_cols = ['price', 'beds', 'baths', 'square_feet']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def load_csv(
    account: str | None = None,
    user: str | None = None,
    password: str | None = None,
    warehouse: str | None = None,
    database: str | None = None,
    schema: str | None = None,
    role: str | None = None,
    csv_path: str | None = None,
) -> None:
    """Load the CSV file into a Snowflake table."""
    account = account or os.getenv('SNOWFLAKE_ACCOUNT')
    user = user or os.getenv('SNOWFLAKE_USER')
    password = password or os.getenv('SNOWFLAKE_PASSWORD')
    warehouse = warehouse or os.getenv('SNOWFLAKE_WAREHOUSE')
    database = database or os.getenv('SNOWFLAKE_DATABASE')
    schema = schema or os.getenv('SNOWFLAKE_SCHEMA', 'PUBLIC')
    role = role or os.getenv('SNOWFLAKE_ROLE', 'SYSADMIN')
    csv_path = csv_path or os.getenv('REDFIN_CSV_PATH')

    df = pd.read_csv(csv_path)
    df = clean_columns(df)

    ctx = snowflake.connector.connect(
        account=account,
        user=user,
        password=password,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role,
    )
    try:
        success, nchunks, nrows, _ = write_pandas(
            ctx, df, TABLE_NAME, auto_create_table=False, overwrite=True
        )
        if success:
            print(f"Loaded {nrows} rows into {TABLE_NAME}")
        else:
            print("Load failed")
    finally:
        ctx.close()


if __name__ == '__main__':
    load_csv()
