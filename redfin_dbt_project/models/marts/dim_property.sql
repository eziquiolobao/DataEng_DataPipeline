with source as (
    select * from {{ ref('stg_redfin_sales') }}
)
select
    row_number() over (order by address) as property_id,
    address,
    city,
    state,
    zip_code,
    latitude,
    longitude
from source
group by address, city, state, zip_code, latitude, longitude
