-- DDL for staging table matching Redfin columns
CREATE TABLE IF NOT EXISTS stg_redfin_sales (
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    price NUMERIC,
    beds INTEGER,
    baths NUMERIC,
    square_feet INTEGER,
    sold_date DATE,
    property_type TEXT,
    latitude NUMERIC,
    longitude NUMERIC
);
