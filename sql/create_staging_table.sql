-- DDL for staging table matching Redfin columns
-- Snowflake DDL for staging table matching Redfin columns
CREATE OR REPLACE TABLE stg_house_sales (
    address VARCHAR,
    city VARCHAR,
    zip_code VARCHAR,
    state_or_province VARCHAR,
    property_type VARCHAR,
    price NUMBER,
    beds NUMBER,
    baths NUMBER,
    square_feet NUMBER,
    sold_date VARCHAR,
    lot_size VARCHAR,
    year_built NUMBER,
    latitude NUMBER,
    longitude NUMBER
);
