with source as (
    select * from HOUSEMARKET.MA_HOUSES_ma_houses.stg_house_sales
)
select
    row_number() over (order by address) as property_id,
    address,
    city,
    state_or_province as state,
    zip_code,
    latitude,
    longitude
from source
group by address, city, state, zip_code, latitude, longitude