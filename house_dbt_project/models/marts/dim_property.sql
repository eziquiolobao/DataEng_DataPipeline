with source as (
    select * from {{ ref('stg_house_sales') }}
),
unique_properties as (
    select distinct
        address,
        city,
        state_or_province as state,
        zip_code,
        latitude,
        longitude
    from source
)
select
    row_number() over (order by address) as property_id,
    address,
    city,
    state,
    zip_code,
    latitude,
    longitude
from unique_properties
