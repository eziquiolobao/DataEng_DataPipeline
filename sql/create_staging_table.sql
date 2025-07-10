-- DDL for staging table matching Redfin columns
-- Snowflake DDL for staging table matching Redfin columns
CREATE OR REPLACE TABLE stg_house_sales (
    address VARCHAR,
    city VARCHAR,
    zip_code VARCHAR,
    state_or_province VARCHAR,
    property_type VARCHAR,
    price NUMBER,
    beds INTEGER,
    baths NUMBER,
    square_feet INTEGER,
    sold_date DATE,
    lot_size NUMBER,
    year_built INTEGER,
    latitude NUMBER,
    longitude NUMBER
);
