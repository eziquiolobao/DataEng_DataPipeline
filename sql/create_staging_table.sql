-- DDL for staging table matching Redfin columns
DROP TABLE IF EXISTS stg_redfin_sales;

CREATE TABLE stg_redfin_sales (
    address TEXT,
    city TEXT,
    zip_code TEXT,
    state_or_province TEXT,
    property_type TEXT,
    price NUMERIC,
    beds INTEGER,
    baths NUMERIC,
    square_feet INTEGER,
    sold_date DATE,
    lot_size NUMERIC,
    year_built INTEGER,
    latitude NUMERIC,
    longitude NUMERIC
);
